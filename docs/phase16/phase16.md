Architecture will evolve:
                 Test
                  │
                  ▼
          ┌───────────────┐
          │   Framework   │
          └───────┬───────┘
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
 Configuration  Driver      API
 validation     lifecycle   reliability
       │          │          │
       └──────────┼──────────┘
                  ▼
          Error handling
                  │
                  ▼
        Retry + diagnostics

Final phase:
Test passes
    ↓
finally
    ↓
quit browser


Final Architecture:
                    Test
                     │
                     ▼
              Pytest Fixtures
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Config      Driver       API
       Validation  Lifecycle   Timeout
          │          │          │
          └──────────┼──────────┘
                     ▼
              Error Handling
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       Logging              Controlled
                              Retry
          │
          ▼
       Diagnostics
     Screenshot + Logs