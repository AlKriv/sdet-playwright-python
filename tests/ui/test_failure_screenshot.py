
def test_should_take_screenshot_on_failure(page):
    page.goto(BaseU, wait_until="domcontentloaded")
    assert "THIS_WILL_FAIL" in page.title()
