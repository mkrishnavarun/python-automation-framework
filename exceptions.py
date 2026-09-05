class FrameworkError(Exception):
    """Base exception for framework errors."""


class ConfigurationError(FrameworkError):
    """Raised when framework configuration is invalid."""


class UnsupportedBrowserError(FrameworkError):
    """Raised when an unsupported browser is requested."""