import json
from pathlib import Path
from typing import Any, cast


class JsonReader:
    @staticmethod
    def read(file_path: str) -> dict[str, Any]:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Test data file not found: {path}")

        with open(path, "r", encoding="utf-8") as file:
            data= json.load(file)
            return cast(dict[str, Any], data)
