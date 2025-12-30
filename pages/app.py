from pages.login_page import LoginPage


class App:
    def __init__(self, page):
        self.page = page
        self.login = LoginPage(page)
