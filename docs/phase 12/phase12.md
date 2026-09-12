Phase 12
│
├── GitHub Actions
│
├── Python environment
│
├── Dependency installation
│
├── Environment selection
│
├── Headless browser execution
│
├── Parallel execution
│
├── Test markers
│
├── Smoke pipeline
│
├── Full regression pipeline
│
├── Test reports
│
├── Failure artifacts
│
└── CI-friendly configuration


Final Workflow:
name: Automation Tests

on:
  push:
    branches:
      - main
      - develop

  pull_request:
    branches:
      - main
      - develop

  workflow_dispatch:

jobs:

  test:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          mkdir -p reports
          pytest \
            --env qa \
            --headless \
            -n 4 \
            -v \
            --html=reports/report.html \
            --self-contained-html

      - name: Upload test report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: pytest-report
          path: reports/report.html

      - name: Upload automation logs
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: automation-logs
          path: logs/


Docker:
Your laptop
     │
     │ docker run
     ▼
┌─────────────────────────────┐
│ Docker Container            │
│                             │
│ Python 3.12                 │
│ Chromium                    │
│ ChromeDriver                │
│ pytest                      │
│ Selenium                    │
│ Your framework              │
│                             │
│       pytest                │
│          ↓                  │
│      API + UI tests         │
└─────────────────────────────┘

3. Why is Docker is useful for framework:
Before:

Developer machine
    ↓
Python version
    ↓
Installed packages
    ↓
Chrome installation
    ↓
Environment differences
    ↓
Tests


After:
Dockerfile
    ↓
Known Python version
    ↓
Known dependencies
    ↓
Known browser
    ↓
Known test environment
    ↓
Tests


Final:

                 Docker
                   │
                   ▼
        ┌─────────────────────┐
        │ python-automation-  │
        │ framework container  │
        │                     │
        │ Python 3.12         │
        │ Chromium            │
        │ Selenium            │
        │ pytest              │
        │ API framework       │
        │ UI framework        │
        └──────────┬──────────┘
                   │
                   ▼
                pytest
                   │
             ┌─────┴─────┐
             ▼           ▼
          API tests    UI tests