import argparse
import os
from pathlib import Path
from typing import Any, Dict, List

import yaml
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM


BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = BASE_DIR / "outputs"


AGENT_KEY_BY_STEP: Dict[int, str] = {
    1: "domain_understanding_analyst",
    2: "domain_structuring_analyst",
}


def load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Fichier YAML introuvable : {path}")

    with path.open("r", encoding="utf-8") as file:
        content = yaml.safe_load(file)

    if not isinstance(content, dict):
        raise ValueError(f"Le fichier YAML est vide ou invalide : {path}")

    return content


def load_inputs_from_directory(input_dir: Path) -> str:
    if not input_dir.exists():
        raise FileNotFoundError(f"Dossier d'entrée introuvable : {input_dir}")

    allowed_extensions = {".md", ".txt", ".log", ".csv"}

    files = sorted(
        file
        for file in input_dir.iterdir()
        if file.is_file() and file.suffix.lower() in allowed_extensions
    )

    if not files:
        raise ValueError(
            f"Aucun fichier exploitable trouvé dans {input_dir}. "
            f"Extensions acceptées : {', '.join(sorted(allowed_extensions))}"
        )

    blocks: List[str] = []

    for file in files:
        content = file.read_text(encoding="utf-8").strip()

        if not content:
            continue

        blocks.append(
            f"""
==============================
SOURCE : {file.name}
CHEMIN : {file.relative_to(BASE_DIR)}
==============================

{content}
""".strip()
        )

    if not blocks:
        raise ValueError(f"Les fichiers trouvés dans {input_dir} sont vides.")

    return "\n\n".join(blocks)


def load_previous_outputs(output_dir: Path, current_step: int) -> str:
    """
    Charge les livrables Markdown des étapes strictement antérieures
    à `current_step` comme contexte. Lit les sous-dossiers `etape-N/`.
    """
    if not output_dir.exists():
        return ""

    blocks: List[str] = []

    for n in range(1, current_step):
        step_dir = output_dir / f"etape-{n}"
        if not step_dir.exists():
            continue

        files = sorted(
            file for file in step_dir.iterdir()
            if file.is_file() and file.suffix.lower() == ".md"
        )

        for file in files:
            content = file.read_text(encoding="utf-8").strip()
            if not content:
                continue
            blocks.append(
                f"""
==============================
LIVRABLE ÉTAPE {n} : {file.name}
==============================

{content}
""".strip()
            )

    return "\n\n".join(blocks)


def build_task_description(
    base_description: str,
    input_text: str,
    previous_outputs: str,
    step: int,
) -> str:
    previous_section = ""
    if previous_outputs:
        previous_section = f"""

---
LIVRABLES DES ÉTAPES PRÉCÉDENTES
---
{previous_outputs}
"""

    step_constraints = {
        1: (
            "- Rester strictement dans l'étape 1 : compréhension du domaine métier.\n"
            "- Ne pas produire de modèle DDD détaillé.\n"
            "- Ne pas produire de schéma d'architecture technique."
        ),
        2: (
            "- Rester strictement dans l'étape 2 : structuration fine du domaine "
            "(acteurs, responsabilités, règles métier, conflits d'objectifs).\n"
            "- S'appuyer sur les livrables de l'étape 1 fournis ci-dessus.\n"
            "- Ne pas produire de modèle DDD détaillé (entités, agrégats, "
            "value objects, événements) — c'est l'étape 3.\n"
            "- Ne pas produire de schéma d'architecture technique."
        ),
    }

    constraints = step_constraints.get(step, step_constraints[1])

    return f"""
{base_description}

---
CORPUS MÉTIER À ANALYSER
---
{input_text}{previous_section}

---
CONSIGNES GÉNÉRALES
---
{constraints}
- Ne pas inventer d'information clinique absente du corpus.
- Distinguer explicitement les faits, les hypothèses et les points à clarifier.
- Identifier les éventuelles contradictions entre les sources.
- Citer les sources utilisées quand c'est utile.
- Produire une réponse en français, structurée en Markdown.
""".strip()


def ensure_project_structure() -> None:
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_agent(agents_config: Dict[str, Any], llm: LLM, step: int) -> Agent:
    agent_key = AGENT_KEY_BY_STEP.get(step)
    if agent_key is None:
        raise ValueError(f"Étape non supportée : {step}")

    if agent_key not in agents_config:
        raise KeyError(f"Agent absent dans agents_step{step}.yaml : {agent_key}")

    agent_config = agents_config[agent_key]

    required_fields = ["role", "goal", "backstory"]
    for field in required_fields:
        if field not in agent_config:
            raise KeyError(f"Champ manquant pour l'agent {agent_key} : {field}")

    return Agent(
        role=agent_config["role"],
        goal=agent_config["goal"],
        backstory=agent_config["backstory"],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def build_tasks(
    tasks_config: Dict[str, Any],
    domain_agent: Agent,
    input_text: str,
    previous_outputs: str,
    step: int,
) -> List[Task]:
    tasks: List[Task] = []

    for task_key, task_config in tasks_config.items():
        required_fields = ["description", "expected_output", "output_file"]

        for field in required_fields:
            if field not in task_config:
                raise KeyError(f"Champ manquant dans la tâche {task_key} : {field}")

        output_file = task_config["output_file"]
        output_path = Path(output_file)

        if output_path.is_absolute():
            raise ValueError(
                f"La tâche {task_key} utilise un chemin absolu interdit : {output_file}. "
                "Utilise un chemin relatif du type outputs/nom_du_fichier.md"
            )

        if output_path.parts[0] != "outputs":
            output_path = Path("outputs") / output_path

        absolute_output_parent = BASE_DIR / output_path.parent
        absolute_output_parent.mkdir(parents=True, exist_ok=True)

        task = Task(
            description=build_task_description(
                task_config["description"],
                input_text,
                previous_outputs,
                step,
            ),
            expected_output=task_config["expected_output"],
            agent=domain_agent,
            output_file=str(output_path),
        )

        tasks.append(task)

    if not tasks:
        raise ValueError(f"Aucune tâche définie dans tasks_step{step}.yaml")

    return tasks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Runner DDD multi-étapes.")
    parser.add_argument(
        "--step",
        type=int,
        default=int(os.getenv("DDD_STEP", "1")),
        choices=sorted(AGENT_KEY_BY_STEP.keys()),
        help="Étape DDD à exécuter (1 = compréhension, 2 = structuration).",
    )
    return parser.parse_args()


DEFAULT_MISTRAL_MODEL = "mistral/mistral-small-latest"


def resolve_mistral_model() -> str:
    """
    Vérifie la présence de MISTRAL_API_KEY et retourne le modèle Mistral à utiliser.
    Le modèle peut être surchargé via LLM_MODEL (doit commencer par 'mistral/').
    """
    if not os.getenv("MISTRAL_API_KEY"):
        raise EnvironmentError(
            "MISTRAL_API_KEY est absent. Définis-le dans .env à la racine du projet."
        )

    model_name = os.getenv("LLM_MODEL", DEFAULT_MISTRAL_MODEL)

    if not model_name.startswith("mistral/"):
        raise ValueError(
            f"Seul le provider Mistral est supporté. LLM_MODEL doit commencer "
            f"par 'mistral/' (reçu : '{model_name}')."
        )

    return model_name


def main() -> None:
    os.chdir(BASE_DIR)
    args = parse_args()
    step = args.step

    load_dotenv(BASE_DIR / ".env")

    model_name = resolve_mistral_model()

    ensure_project_structure()

    agents_path = CONFIG_DIR / f"agents_step{step}.yaml"
    tasks_path = CONFIG_DIR / f"tasks_step{step}.yaml"

    agents_config = load_yaml(agents_path)
    tasks_config = load_yaml(tasks_path)

    input_text = load_inputs_from_directory(INPUT_DIR)
    previous_outputs = load_previous_outputs(OUTPUT_DIR, step) if step > 1 else ""

    llm = LLM(model=model_name)

    domain_agent = build_agent(agents_config, llm, step)
    tasks = build_tasks(tasks_config, domain_agent, input_text, previous_outputs, step)

    crew = Crew(
        agents=[domain_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )

    print(f"\n=== Étape {step} : {AGENT_KEY_BY_STEP[step]} ===")
    print(f"Modèle LLM : {model_name}")
    print(f"Configs : {agents_path.name}, {tasks_path.name}")
    if previous_outputs:
        print(f"Contexte étapes précédentes : {OUTPUT_DIR.relative_to(BASE_DIR)}")

    result = crew.kickoff()

    print("\nExécution terminée.")
    print(f"Sources analysées depuis : {INPUT_DIR.relative_to(BASE_DIR)}")
    print(f"Livrables générés dans : {OUTPUT_DIR.relative_to(BASE_DIR)}")

    print("\nFichiers de sortie attendus :")
    for task_config in tasks_config.values():
        output_file = Path(task_config["output_file"])

        if not output_file.is_absolute() and output_file.parts[0] != "outputs":
            output_file = Path("outputs") / output_file

        print(f"- {output_file}")

    print("\nRésultat global :")
    print(result)


if __name__ == "__main__":
    main()
