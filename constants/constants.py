from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

REPORTS_DIRECTORY = PROJECT_ROOT / "reports"

SCREENSHOTS_DIRECTORY = (
    REPORTS_DIRECTORY / "screenshots"
)

LOGS_DIRECTORY = PROJECT_ROOT / "logs"