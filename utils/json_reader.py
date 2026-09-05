import json
from pathlib import Path


class JsonReader:

    @staticmethod
    def read(file_path: str) -> dict:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Test data file not found: {path}"
            )

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)