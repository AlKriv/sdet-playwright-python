from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page
        self.heading = page.locator("h1")

    def is_loaded(self) -> bool:
        # Simple, stable check that page is rendered
        return self.heading.first.is_visible()

    def title_contains(self, text: str) -> None:
        # Assertion helper for readable tests
        expect(self.page).to_have_title(lambda t: text in t)
