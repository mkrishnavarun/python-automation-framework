Advanced Reporting:
Test failure
    ↓
Screenshot
    +
Logs
    +
HTML report
    ↓
CI artifact

After Phase 14:
                    TEST
                     │
                     ▼
                  pytest
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       Success                Failure
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
                 Screenshot    Logs      HTML Report
                    │           │           │
                    └───────────┼───────────┘
                                ▼
                         CI Artifacts