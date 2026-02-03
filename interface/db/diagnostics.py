import subprocess
from pathlib import Path


def get_repo_root() -> Path:
    try:
        out = subprocess.check_output([
            "git",
            "rev-parse",
            "--show-toplevel",
        ], text=True).strip()
        return Path(out)
    except Exception:
        return Path(__file__).resolve().parents[2]


def summarize_folder(path: Path) -> dict:
    total_entries = 0
    json_files = 0
    yaml_files = 0
    subdirs = 0
    if not path.exists():
        return {
            "total_entries": 0,
            "json_files": 0,
            "yaml_files": 0,
            "subdirs": 0,
        }
    for entry in path.iterdir():
        if entry.name.startswith("."):
            continue
        total_entries += 1
        if entry.is_dir():
            subdirs += 1
        elif entry.is_file():
            if entry.suffix.lower() == ".json":
                json_files += 1
            elif entry.suffix.lower() in {".yaml", ".yml"}:
                yaml_files += 1
    return {
        "total_entries": total_entries,
        "json_files": json_files,
        "yaml_files": yaml_files,
        "subdirs": subdirs,
    }


def main():
    repo_root = get_repo_root()
    validated_dir = repo_root / "artifacts" / "validated"
    folders = [
        "authority_reference",
        "evidence_item",
        "money_flow",
        "field_validation",
    ]

    print("Diagnostics: artifacts/validated (top-level only)")
    for folder in folders:
        stats = summarize_folder(validated_dir / folder)
        print(
            f"{folder}: total_entries={stats['total_entries']} | "
            f"json_files={stats['json_files']} | yaml_files={stats['yaml_files']} | "
            f"subdirs={stats['subdirs']}"
        )


if __name__ == "__main__":
    main()
