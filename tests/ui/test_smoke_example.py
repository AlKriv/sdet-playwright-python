import pytest


@pytest.mark.ui
@pytest.mark.smoke
def test_example_dot_com_title(app):
    app.login.open()
    assert "Example" in app.page.title()
