Developer Push / PR
        │
        ▼
GitHub Actions
        │
        ├── Checkout
        │
        ├── Setup Python
        │
        ├── Install Dependencies
        │
        ├───────────────┐
        │               │
        ▼               ▼
   Code Quality       Tests
   Ruff               Pytest
   Mypy               xdist
        │               │
        └───────┬───────┘
                │
                ▼
          Test Results
                │
       ┌────────┼─────────┐
       ▼        ▼         ▼
     HTML    Screenshots Logs
    Report
       │        │         │
       └────────┴─────────┘
                │
                ▼
         CI Artifacts