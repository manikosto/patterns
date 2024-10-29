from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.signup_page import SignupPage
# from data.subjects import Emails

class BaseTest:

    def setup_method(self):
        # self.emails = Emails()

        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.signup_page = SignupPage(self.driver)


