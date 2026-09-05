tests
  │
  │ uses
  ▼
Page Objects
  │
  │ inherit from
  ▼
BasePage
  │
  │ uses
  ▼
WebDriver
  │
  │ created by
  ▼
DriverFactory


In Code:
test_login.py
      │
      ▼
LoginPage
      │
      ▼
BasePage
      │
      ▼
WebDriver
      ▲
      │
DriverFactory
      ▲
      │
driver fixture