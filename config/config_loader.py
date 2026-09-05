from pathlib import Path

import yaml

from config.models import (
    ApplicationConfig,
    BrowserConfig,
    EnvironmentConfig,
    APIConfig
)


class ConfigLoader:

    @staticmethod
    def load(environment: str) -> EnvironmentConfig:
        project_root = Path(__file__).resolve().parents[1]

        config_file = (
            project_root
            / "config"
            / f"{environment}.yaml"
        )

        if not config_file.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_file}"
            )

        with open(config_file, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return EnvironmentConfig(
            environment=data["environment"],
            application=ApplicationConfig(
                base_url=data["application"]["base_url"]
            ),
            browser=BrowserConfig(
                timeout=data["browser"]["timeout"]
            ),
            api=APIConfig(
                base_url=data["api"]["base_url"],
                timeout=data["api"]["timeout"]
            )
        )