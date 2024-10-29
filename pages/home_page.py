import allure
from base.base_page import BasePage
from data.links import Links
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    _PAGE_URL = Links.HOME_PAGE

    _POST_AREA = "//textarea[@name='post']"
    _POST_BUTTON = "//input[@value='Post']"
    _POST_MENU = "(//div[contains(@id, 'activity-item')])[1]//div[@class='post-menu']"
    _DELETE_POST_BUTTON = "(//div[contains(@id, 'activity-item')])[1]//div[@class='post-menu']//a[text()='Delete']"

    @allure.step("Write new post")
    def write_post(self, text):
        area = self.driver.find_element(*self._POST_AREA)
        area.send_keys(text)
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="example",
            attachment_type=allure.attachment_type.PNG
        )
        assert area.get_attribute("value") == text, "Пост не написан"
        return self

    @allure.step("Post")
    def post(self):
        self.driver.find_element(*self._POST_BUTTON).click()
        return self

    @allure.step("Delete post as admin")
    def delete_post_as_admin(self):
        self.driver.find_element(*self._POST_MENU).click()
        self.wait.until(EC.element_to_be_clickable(self._DELETE_POST_BUTTON)).click()
        return self

    @allure.step("Mark post as admin")
    def mark_post_as_admin(self):
        ...