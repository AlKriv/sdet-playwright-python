import pytest

@pytest.mark.ui
@pytest.mark.smoke
def test_home_page_loads(app):
    app.login.open()
    assert app.home.is_loaded()

@pytest.mark.ui
@pytest.mark.smoke
def test_home_title_contains_example(app):
    app.login.open()
    app.home.title_contains("Example")
