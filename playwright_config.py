import os

from dotenv import load_dotenv

load_dotenv()

CONTEXT_CONFIG = {
    "base_url": os.environ['BASE_URL'],
    "viewport": {'width': 1920, 'height': 1080},
    "locale": 'de-DE',
    "timezone_id": 'Europe/Berlin',
}

BROWSER_CONFIG = {
    "headless": True
}

UTILS_CONFIG = {
    "expect_timeout": 10000,
    "browser": os.environ['BROWSER'],
    "trace": os.environ['TRACE'],
    "base_url_api": os.environ['BASE_URL'],
    "report_path": "reports"
}
