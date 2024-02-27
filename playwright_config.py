import os

from dotenv import load_dotenv


def load_env():
    env = os.environ.get("ENV")
    if env:
        load_dotenv(f".env.{env}")
    else:
        load_dotenv(".env")


load_env()

CONTEXT_CONFIG = {
    "base_url": os.environ["BASE_URL"],
    "viewport": {"width": 1920, "height": 1080},
    "locale": "de-DE",
    "timezone_id": "Europe/Berlin",
    "storage_state": "state.json"
}

BROWSER_CONFIG = {"headless": False, "slow_mo": 0.0}

UTILS_CONFIG = {
    "expect_timeout": 10000,
    "browser": os.environ["BROWSER"],
    "trace": os.environ["TRACE"],
    "base_url_api": os.environ["BASE_URL_API"],
    "report_path": "reports",
}
