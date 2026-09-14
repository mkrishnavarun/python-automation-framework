# Python Automation Framework

A scalable test automation framework built using Python, Pytest,
Selenium, REST API automation, Docker and GitHub Actions.

The framework demonstrates UI automation, API automation,
configuration management, test data management, parallel execution,
CI/CD integration, failure diagnostics and code quality practices.

---

## Tech Stack

- Python 3.12
- Pytest
- Selenium
- Requests
- Pytest-Xdist
- Pytest-HTML
- Pytest-Rerunfailures
- Docker
- GitHub Actions
- Ruff
- Mypy

---

## Key Features

- Page Object Model
- UI automation
- REST API automation
- API service layer
- Typed configuration models
- Environment-based configuration
- Centralized test data management
- Factory-based test data generation
- Browser factory
- Reusable Pytest fixtures
- Parallel execution
- Failure screenshots
- Centralized logging
- HTML test reporting
- API/UI test separation
- Test isolation
- Docker execution
- CI/CD using GitHub Actions
- Static analysis using Ruff
- Type checking using Mypy
- Custom framework exceptions
- API timeout/error handling
- Controlled test retry capability

---

## Architecture

The framework follows a layered architecture:

Tests
↓
Fixtures
↓
Pages / Services
↓
Framework Core
↓
External Systems

UI tests communicate through Page Objects.

API tests communicate through Service Objects.

Common framework functionality such as configuration,
logging, drivers and test data is centralized.

---

## Project Structure

framework/
├── api/
├── config/
├── drivers/
├── fixtures/
├── models/
├── pages/
├── services/
└── utils/

tests/
├── api/
├── ui/
└── unit/

---

## Running Locally

Create a virtual environment:

python -m venv .venv

Activate it:

Linux/macOS:

source .venv/bin/activate

Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the complete suite:

pytest --env qa -v

Run UI tests headlessly:

pytest --env qa --headless -v

Run tests in parallel:

pytest --env qa --headless -n 4 -v

---

## Browser Selection

Chrome:

pytest --env qa --browser chrome --headless

Firefox:

pytest --env qa --browser firefox --headless

---

## HTML Reporting

pytest \
    --env qa \
    --headless \
    --html=reports/report.html \
    --self-contained-html

Failure screenshots are automatically stored under:

reports/screenshots/

---

## Docker

Build the image:

docker build -t python-automation-framework .

Run the framework:

docker run --rm \
    -v "$(pwd)/reports:/app/reports" \
    python-automation-framework

---

## CI/CD

GitHub Actions automatically:

1. Checks out the repository
2. Installs Python
3. Installs dependencies
4. Runs code-quality checks
5. Executes automated tests
6. Generates test reports
7. Uploads reports and logs as artifacts

---

## Design Patterns

The framework demonstrates several commonly used patterns:

### Factory Pattern

DriverFactory creates the required browser driver.

### Page Object Model

Each application page encapsulates its locators and operations.

### Service Layer Pattern

API business operations are separated from low-level HTTP handling.

### Singleton-style Resource Management

Shared framework resources can be centrally managed where appropriate.

### Builder/Data Factory Pattern

TestDataFactory creates unique test data for tests.

### Dependency Injection

Pytest fixtures inject configuration, drivers, API clients,
services and test data into tests.

---

## Failure Handling

When a UI test fails:

1. Pytest identifies the failed test.
2. The framework captures a screenshot.
3. Failure information is logged.
4. HTML report contains the test result.
5. CI uploads diagnostic artifacts.

This makes failures easier to investigate.

---

## Parallel Execution

Pytest-xdist is used to execute tests across multiple workers.

Example:

pytest -n 4

Tests are designed to be isolated so that parallel execution
does not create shared-state problems.

---

## Configuration

Environment-specific configuration is stored separately.

Example:

config/qa.yaml

config/staging.yaml

Tests select the environment using:

pytest --env qa

The configuration is loaded into typed dataclass models.

---

## Quality Checks

Ruff:

ruff check .

Ruff formatting:

ruff format --check .

Mypy:

mypy framework

These checks are also executed in CI.

---

## Engineering Principles

The framework focuses on:

- Maintainability
- Reusability
- Separation of concerns
- Test isolation
- Failure diagnostics
- Environment independence
- Parallel execution
- CI/CD compatibility
- Type safety
- Clean code

## Architecture Diagram
                         ┌─────────────────────┐
                         │      Test Cases     │
                         │                     │
                         │ UI / API / Unit     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Pytest Fixtures   │
                         │                     │
                         │ Config / Driver     │
                         │ API / Services      │
                         │ Test Data           │
                         └──────────┬──────────┘
                                    │
                  ┌─────────────────┴─────────────────┐
                  │                                   │
                  ▼                                   ▼
        ┌──────────────────┐                ┌──────────────────┐
        │    UI Layer      │                │    API Layer     │
        │                  │                │                  │
        │ Page Objects     │                │ Service Objects  │
        │ BasePage         │                │ API Client       │
        └────────┬─────────┘                └────────┬─────────┘
                 │                                   │
                 ▼                                   ▼
        ┌──────────────────┐                ┌──────────────────┐
        │    Selenium      │                │      REST API    │
        └──────────────────┘                └──────────────────┘


                    Shared Framework Components

       ┌────────────┬────────────┬────────────┬────────────┐
       │ Config     │ Logging    │ Test Data  │ Exceptions │
       └────────────┴────────────┴────────────┴────────────┘


                         Execution Layer

       ┌───────────────────────────────────────────────────┐
       │ Pytest → xdist → Docker → GitHub Actions → Report │
       └───────────────────────────────────────────────────┘

## Design Decisions

### Why Page Object Model?

To separate UI interaction logic from test scenarios
and reduce duplication.

### Why a Service Layer?

To prevent tests from depending directly on HTTP implementation
details.

### Why typed configuration?

To make configuration access explicit and reduce errors caused
by dictionary-based configuration.

### Why Pytest fixtures?

To provide reusable dependencies and lifecycle management.

### Why parallel execution?

To reduce overall execution time as the test suite grows.

### Why Docker?

To provide a reproducible execution environment.

### Why CI artifacts?

To preserve failure diagnostics even when tests execute remotely.


## Future Improvements

- Selenium Grid / remote browser execution
- API schema validation
- Allure reporting
- Secrets management
- Database utilities
- Cloud execution
- Test tagging and selective pipelines
- Distributed test execution
- Slack/Teams notifications
- Historical test analytics
- Automatic flaky-test detection