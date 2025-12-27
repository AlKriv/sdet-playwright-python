from playwright.sync_api import sync_playwright

def test_example_dot_com_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com", wait_until="domcontentloaded")
        assert "Example" in page.title()
        browser.close()