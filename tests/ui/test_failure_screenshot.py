import pytest

@pytest.mark.debug
def test_should_take_screenshot_on_failure(app):
    app.login.open()
    assert "THIS_WILL_FAIL" in app.page.title()
