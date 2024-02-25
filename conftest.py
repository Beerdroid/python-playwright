import pendulum
from _pytest.fixtures import fixture
from playwright.sync_api import Page, sync_playwright, expect

from playwright_config import *
from src.pages.app import App

load_dotenv()

# custom timeout for assertions
expect.set_options(timeout=UTILS_CONFIG.get('expect_timeout'))



def get_browser(get_playwright, browser):
    match browser:
        case "chromium":
            return get_playwright.chromium
        case "webkit":
            return get_playwright.webkit
        case "firefox":
            return get_playwright.firefox
        case _:
            raise ValueError(f"Unsupported browser: {browser}")


@fixture(scope="function")
def new_page(get_playwright, request) -> Page:
    browser = get_browser(get_playwright, UTILS_CONFIG.get("browser")).launch(**BROWSER_CONFIG)
    context = browser.new_context(**CONTEXT_CONFIG)

    trace = UTILS_CONFIG.get("trace")
    if trace in ['retain-on-failure', 'on']:
        context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()
    yield page

    trace_name = f'./trace/run_{pendulum.now('UTC').format("YYYY_MM_DD-HH_mm")}/trace_{request.node.name}.zip'

    if trace == 'retain-on-failure' and request.node.rep_call.failed:
        context.tracing.stop(path=trace_name)
    elif trace == 'on':
        context.tracing.stop(path=trace_name)

    context.close()


@fixture(scope="function")
def new_request_context(get_playwright):
    request_context = get_playwright.request.new_context(base_url=UTILS_CONFIG.get("base_url_api"))
    yield request_context
    request_context.dispose()


@fixture(scope="session")
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='function')
def app(new_page, new_request_context):
    yield App(new_page, new_request_context)
