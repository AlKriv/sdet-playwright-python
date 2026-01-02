from pages.login_page import LoginPage
from pages.home_page import HomePage


class App:
    def __init__(self, page):
        self.page = page
        self.login = LoginPage(page)
        self.home = HomePage(page)
