import allure
import pickle
import os
import allure
from base.base_page import BasePage
from data.links import Links
from pages.home_page import HomePage

class LoginPage(BasePage):

    _PAGE_URL = Links.LOGIN_PAGE

    _LOGIN_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"
    _SUBMIT_BUTTON = "//input[@type='submit']"

    # def login(self):
    #     LOGIN = self.credentials.USER_LOGIN
    #     PASSWORD = self.credentials.USER_PASSWORD
    #
    #     login_field = self.driver.find_element(*self._LOGIN_FIELD)
    #     login_field.clear()
    #     login_field.send_keys(LOGIN)
    #
    #     password_field = self.driver.find_element(*self._PASSWORD_FIELD)
    #     password_field.clear()
    #     password_field.send_keys(PASSWORD)
    #
    #     self.driver.find_element(*self._SUBMIT_BUTTON).click()
    #
    #     return HomePage(self.driver)
    def login_as(self, role):
        with allure.step(f"Login as {role}"):
            if role == "admin":
                LOGIN = self.credentials.ADMIN_LOGIN
                PASSWORD = self.credentials.ADMIN_PASSWORD
            elif role == "user":
                LOGIN = self.credentials.USER_LOGIN
                PASSWORD = self.credentials.USER_PASSWORD

            login_field = self.driver.find_element(*self._LOGIN_FIELD)
            login_field.clear()
            login_field.send_keys(LOGIN)

            password_field = self.driver.find_element(*self._PASSWORD_FIELD)
            password_field.clear()
            password_field.send_keys(PASSWORD)

            self.driver.find_element(*self._SUBMIT_BUTTON).click()

