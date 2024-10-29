from base.base_page import BasePage
from data.links import Links

class SignupPage(BasePage):

    _PAGE_URL = Links.HOST

    FIELD_NAME = "//input[@name='firstname']"
    FIELD_FNAME = "//input[@name='lastname']"
    FIELD_EMAIL = "//input[@name='email']"
    FIELD_EMAIL_RE = "//input[@name='email_re']"
    FIELD_USERNAME = "//input[@name='username']"
    FIELD_PASSWORD = "//input[@name='password']"
    FIELD_BIRTH = "//input[@name='birthdate']"
    FIELD_DATE = "//a[@data-date='10']"
    FIELD_MALE = "//input[@value='male']"
    FIELD_GDPR = "//input[@name='gdpr_agree']"
    SUBMIT = "//input[@id='ossn-submit-button']"

    def signup_as(self, name, email):
        self.driver.find_element(*self.FIELD_NAME).send_keys(name)
        self.driver.find_element(*self.FIELD_FNAME).send_keys("dfasdfadsf")
        self.driver.find_element(*self.FIELD_EMAIL).send_keys(email)
        self.driver.find_element(*self.FIELD_EMAIL_RE).send_keys(email)
        self.driver.find_element(*self.FIELD_USERNAME).send_keys("insomnia")
        self.driver.find_element(*self.FIELD_PASSWORD).send_keys("fasdfadsf")
        self.driver.find_element(*self.FIELD_BIRTH).click()
        self.driver.find_element(*self.FIELD_DATE).click()
        self.driver.find_element(*self.FIELD_MALE).click()
        self.driver.find_element(*self.FIELD_GDPR).click()
        self.driver.find_element(*self.SUBMIT).click()