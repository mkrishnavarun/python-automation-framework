Our Framework becomes:
Git Push
   ↓
GitHub Actions
   ↓
Code Quality
 ┌─────────────┐
 │ Ruff        │
 │ mypy        │
 └──────┬──────┘
        ↓
Automation Tests
        ↓
Report


Final flow:
             Git Push
                 │
                 ▼
        ┌────────────────┐
        │ GitHub Actions │
        └───────┬────────┘
                │
        ┌───────┴────────┐
        ▼                ▼
     Quality            Tests
        │                │
   Ruff + mypy       pytest
        │                │
        └───────┬────────┘
                ▼
              Result