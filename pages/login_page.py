from config.settings import BASE_URL


class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        # Centralized navigation: tests should not know URLs
        self.page.goto(BASE_URL, wait_until="domcontentloaded")