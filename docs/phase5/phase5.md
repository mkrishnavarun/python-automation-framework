Phase 5:
* Logging, Screenshots and Reporting

Intuition:
Right now, if this fails:

login_page.login("standard_user", "wrong_password")

Pytest tells us the test failed, but our framework should give us much more:

Test Failed
   │
   ├── What test?
   ├── What step?
   ├── What exception?
   ├── When did it happen?
   ├── Screenshot
   └── Report


What are we building?
Logger
                      │
             ┌────────┴────────┐
             ▼                 ▼
        Console             File
        INFO+             DEBUG+
                              │
                              ▼
                    logs/automation.log