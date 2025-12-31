import os
import pytest
from playwright.sync_api import sync_playwright
from pages.app import App
from config.settings import (
    BROWSER,
    HEADLESS,
    ACTION_TIMEOUT_MS,
    NAVIGATION_TIMEOUT_MS,
    VIEWPORT_WIDTH,
    VIEWPORT_HEIGHT
)


@pytest.fixture
def app(page):
    # High-level facade for tests
    return App(page)


@pytest.fixture
def page(request):
    with sync_playwright() as p:

        browser_type = getattr(p, BROWSER, None)
        if browser_type is None:
            raise ValueError(f"Unsupported BROWSER='{BROWSER}'. Use: chromium, firefox, webkit")

        browser = browser_type.launch(headless=HEADLESS)

        # Create isolated browser context for each test (cookies/localStorage separation)
        # Create context with consistent defaults (viewport + timeouts)
        context = browser.new_context(
            viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT},
        )
        # Apply default timeouts for stability
        context.set_default_timeout(ACTION_TIMEOUT_MS)
        context.set_default_navigation_timeout(NAVIGATION_TIMEOUT_MS)
        page = context.new_page()

        # Start tracing for every test, but save the trace only on failure
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield page

        # If the test failed, persist trace to artifacts; otherwise just stop tracing
        rep_call = getattr(request.node, "rep_call", None)
        if rep_call and rep_call.failed:
            os.makedirs("artifacts", exist_ok=True)
            context.tracing.stop(path=f"artifacts/{request.node.name}.zip")
        else:
            context.tracing.stop()

        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Store the test result on the node so fixtures can check pass/fail status
    if rep.when == "call":
        item.rep_call = rep

    # Take screenshot only on test failure (call phase)
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("artifacts", exist_ok=True)
            page.screenshot(path=f"artifacts/{item.name}.png", full_page=True)