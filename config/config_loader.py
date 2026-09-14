from pathlib import Path

import yaml

from config.models import APIConfig, ApplicationConfig, BrowserConfig, EnvironmentConfig


class ConfigLoader:
    @staticmethod
    def load(environment: str) -> EnvironmentConfig:
        project_root = Path(__file__).resolve().parents[1]

        config_file = project_root / "config" / f"{environment}.yaml"

        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

        with open(config_file, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        return EnvironmentConfig(
            environment=data["environment"],
            application=ApplicationConfig(base_url=data["application"]["base_url"]),
            browser=BrowserConfig(timeout=data["browser"]["timeout"]),
            api=APIConfig(base_url=data["api"]["base_url"], timeout=data["api"]["timeout"]),
        )

    @staticmethod
    def _validate(data: dict, environment: str) -> None:
        required_sections = [
            "environment",
            "application",
            "browser",
            "api",
        ]

        for section in required_sections:
            if section not in data:
                raise ConfigurationError(
                    f"Missing '{section}' section in {environment} configuration"
                )

        if not data["application"].get("base_url"):
            raise ConfigurationError(
                "Application base_url is missing"
            )

        if not data["api"].get("base_url"):
            raise ConfigurationError(
                "API base_url is missing"
            )

        if not data["browser"].get("timeout"):
            raise ConfigurationError(
                "Browser timeout is missing"
            )
