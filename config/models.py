from dataclasses import dataclass


@dataclass(frozen=True)
class ApplicationConfig:
    base_url: str


@dataclass(frozen=True)
class BrowserConfig:
    timeout: int

@dataclass(frozen=True)
class APIConfig:
    base_url: str
    timeout: int

@dataclass(frozen=True)
class EnvironmentConfig:
    environment: str
    application: ApplicationConfig
    browser: BrowserConfig
    api: APIConfig
