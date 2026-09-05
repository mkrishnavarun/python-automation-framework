Architecture:
                         TEST
                           │
             ┌─────────────┴─────────────┐
             ↓                           ↓
       API Fixtures                 UI Fixtures
             │                           │
       UserService                   Page Object
             │                           │
        APIClient                     Driver
             │                           │
             └─────────────┬─────────────┘
                           ↓
                    Application/API


Test Life Cycle:

API → Create test data
 ↓
UI → Use test data
 ↓
UI → Perform action
 ↓
API → Verify backend
 ↓
API → Cleanup