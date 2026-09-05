* At the end of phase 8, we have below:
python-automation-framework/
│
├── config/
│   ├── qa.yaml
│   └── staging.yaml
│
├── test_data/
│   └── users.json
│
├── framework/
│   │
│   ├── api/
│   │   ├── api_client.py
│   │   └── response_validator.py
│   │
│   ├── config/
│   │   ├── config_loader.py
│   │   └── models.py
│   │
│   ├── drivers/
│   │   ├── driver_factory.py
│   │   └── browser_options.py
│   │
│   ├── fixtures/
│   │   ├── api.py
│   │   ├── browser.py
│   │   ├── config.py
│   │   ├── data.py
│   │   └── pages.py
│   │
│   ├── pages/
│   │   ├── base_page.py
│   │   └── login_page.py
│   │
│   └── utils/
│       ├── json_reader.py
│       └── logger.py
│
├── tests/
│   ├── api/
│   │   └── test_users.py
│   │
│   ├── ui/
│   │   └── test_login.py
│   │
│   └── unit/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

* We have succesfully created API tests and Framework