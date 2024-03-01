# Python Playwright POC

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An example of an automation project with Web UI and Rest API tests

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Changelog](#changelog)
- [Support](#support)
- [Examples](#examples)
- [References](#references)

## Installation

### Prerequisites

- Python 3.x
- Java SDK for Allure report generation

### Instructions

Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Execute the command to run all test or a specific scope:

```bash
pytest

# Based on pytest.ini markers
pytest -m ui
pytest -m api
```
Refer to reports/{date}/report_{time}.html for an automatically generated simple report

Execute the command to generate an additional Allure report:

```bash
# Single file html
allure generate --single-file reports/allure --clean
```

### Configuration
Use playwright_config.py for specific playwright browser, context and misc config

Use pytest.ini env section to load a specific .env file
```bash
[pytest]
#Environment variables
env =
    ENV = test
```

Use pytest.ini 'addopts' property to configure pytest command line default arguments