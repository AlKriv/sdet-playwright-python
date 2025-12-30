

def test_example_dot_com_title(page):
    page.goto("https://example.com", wait_until="domcontentloaded")
    assert "Example" in page.title()
