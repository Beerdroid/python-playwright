import os
import time
from datetime import datetime
from pathlib import Path

import pytest
from _pytest.fixtures import fixture
from playwright.sync_api import Page, sync_playwright, expect
from pytest_playwright_visual.plugin import assert_snapshot

from playwright_config import CONTEXT_CONFIG, BROWSER_CONFIG, UTILS_CONFIG
from src.helpers.api.api import Api
from src.pages.ui import Ui
from src.pages.login_page import LoginPage

# custom timeout for assertions
expect.set_options(timeout=UTILS_CONFIG.get("expect_timeout"))


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


@fixture(scope="session")
def get_storage_state(get_browser):
    context = get_browser.new_context(base_url=CONTEXT_CONFIG.get("base_url"))

    page = context.new_page()
    page.goto('/')

    login = LoginPage(page)
    login.fill_credentials(os.getenv("USER_LOGIN"), os.getenv("PASSWORD"))
    login.submit_login()
    time.sleep(3)

    context.storage_state(path=CONTEXT_CONFIG.get("storage_state"))
    yield context

    context.close()


@fixture(scope="function")
def get_page(get_browser, get_storage_state, request) -> Page:
    context = get_browser.new_context(**CONTEXT_CONFIG)

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
def ui(get_page, assert_snapshot):
    yield Ui(get_page, assert_snapshot)


@fixture(scope="function")
def api(get_request_context):
    yield Api(get_request_context)


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
