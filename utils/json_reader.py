import json
from pathlib import Path
from typing import Any


class JsonReader:
    @staticmethod
    def read(file_path: str) -> dict[str, Any]:
        path = Path(file_path)

        # Resolve relative paths from the project root
        if not path.is_absolute():
            project_root = Path(__file__).resolve().parents[1]
            path = project_root / path

        if not path.exists():
            raise FileNotFoundError(f"Test data file not found: {path}")

        with path.open("r", encoding="utf-8") as file:
            return dict(json.load(file))
