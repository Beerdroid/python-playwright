import os
import time
from datetime import datetime
from pathlib import Path

import pytest
from _pytest.fixtures import fixture
from playwright.sync_api import sync_playwright, expect

from playwright_config import CONTEXT_CONFIG, BROWSER_CONFIG, UTILS_CONFIG
from src.helpers.api.api import Api
from src.models.state import State, Role, Login
from src.pages.login_page import LoginPage
from src.pages.ui import Ui

# custom timeout for assertions
expect.set_options(timeout=UTILS_CONFIG.get("expect_timeout"))
state_dir = UTILS_CONFIG["state_dir"]


def get_driver(get_playwright, browser):
    match browser:
        case "chromium":
            return get_playwright.chromium
        case "webkit":
            return get_playwright.webkit
        case "firefox":
            return get_playwright.firefox
        case _:
            raise ValueError(f"Unsupported browser: {browser}")


@fixture(scope="session")
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope="session")
def get_browser(get_playwright):
    browser = get_driver(get_playwright, UTILS_CONFIG.get("browser")).launch(
        **BROWSER_CONFIG)

    yield browser
    browser.close()


@fixture(scope="session", autouse=True)
def create_storage_states(get_browser):
    for role in Role:
        context = get_browser.new_context(base_url=CONTEXT_CONFIG.get("base_url"))

        page = context.new_page()

        login = LoginPage(page)
        login.goto()
        login.fill_credentials(os.getenv(Login[role.value].value), os.getenv("PASSWORD"))
        login.submit_login()
        time.sleep(3)

        if not os.path.exists(state_dir):
            os.makedirs(state_dir)
        file_path = os.path.join(state_dir, State[role.value].value)
        context.storage_state(path=file_path)

        context.close()


@fixture(scope="function")
def get_page(get_browser, request):
    file_path = os.path.join(state_dir, State[Role.MAIN_USER.value].value)
    context = get_browser.new_context(**CONTEXT_CONFIG, storage_state=file_path)

    trace = UTILS_CONFIG.get("trace")
    if trace in ["retain-on-failure", "on"]:
        context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()
    yield page

    now = datetime.now()
    formatted_date_time = now.strftime("%Y_%m_%d-%H_%M")
    trace_name = f"./trace/run_{formatted_date_time}/trace_{request.node.name}.zip"

    if trace == "retain-on-failure" and request.node.rep_call.failed:
        context.tracing.stop(path=trace_name)
    elif trace == "on":
        context.tracing.stop(path=trace_name)

    context.close()


@fixture(scope="function")
def get_request_context(get_playwright):
    request_context = get_playwright.request.new_context(
        base_url=UTILS_CONFIG.get("base_url_api")
    )
    yield request_context
    request_context.dispose()


@fixture(scope="function")
def ui(get_page):
    yield Ui(get_page)


@fixture(scope="function")
def api(get_request_context):
    yield Api(get_request_context)


@pytest.fixture
def ui_factory(get_browser, request):
    contexts = {}
    trace = UTILS_CONFIG.get("trace")

    def _ui_factory(role: Role):
        file_path = os.path.join(UTILS_CONFIG["state_dir"], State[role.value].value)
        contextInstance = get_browser.new_context(**CONTEXT_CONFIG, storage_state=file_path)

        if trace in ["retain-on-failure", "on"]:
            contextInstance.tracing.start(screenshots=True, snapshots=True)

        page = contextInstance.new_page()
        ui_instance = Ui(page)

        contexts[role.value] = contextInstance
        return ui_instance

    yield _ui_factory

    for roleValue, context in contexts.items():
        now = datetime.now()
        formatted_date_time = now.strftime("%Y_%m_%d-%H_%M")
        trace_name = f"./trace/run_{formatted_date_time}/trace_{request.node.name}_{roleValue}.zip"

        if trace == "retain-on-failure" and request.node.rep_call.failed:
            context.tracing.stop(path=trace_name)
        elif trace == "on":
            context.tracing.stop(path=trace_name)

        context.close()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # set custom options only if none are provided from command line
    if not config.option.htmlpath:
        now = datetime.now()
        # create report target dir
        reports_dir = Path(UTILS_CONFIG.get("report_path"), now.strftime("%Y_%m_%d"))
        reports_dir.mkdir(parents=True, exist_ok=True)
        # custom report file
        report = reports_dir / f"report_{now.strftime('%H_%M')}.html"
        # adjust plugin options
        config.option.htmlpath = report
        config.option.self_contained_html = True
