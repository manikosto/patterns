import allure
import time
import pytest
from base.base_test import BaseTest


class TestExample(BaseTest):

    # def test_example(self):
    #     (self.login_page
    #      .open()
    #      .login()
    #      .write_post("cfasdf")
    #      .post()
    #      )

    # def test_example(self):
    #     self.signup_page.open()
    #     subject = self.emails.verification_email.get_subject("Aleksei")
    #     mail = Mailchecker(subject_for_deletion=subject)
    #     self.signup_page.signup_as("Ivanko", "manikosto@gmail.com")
    #     link = mail.search_emails(
    #         self.emails.verification_email.regexp,
    #         subject
    #     )
    #     self.driver.get(link)
    #     time.sleep(5)


    # @pytest.mark.parametrize("add_users", [1], indirect=True)
    # def test_example_user(self, add_users):
    #     user_2 = add_users
    #     self.login_page.open()
    #     user_2.login_page.open()

    # @allure.title("Create and post new content")
    # def test_create_and_post_new_content_as_user(self):
    #     self.login_page.open()
    #     self.login_page.login_as("user")
    #     self.home_page.write_post("Hey, I'm Alex")
    #     self.home_page.post()
    #     time.sleep(5)
    #
    # @allure.title("Delete post as admin")
    # def test_delete_post_as_admin(self):
    #     self.login_page.open()
    #     self.login_page.login_as("admin")
    #     self.home_page.delete_post_as_admin()
    #     time.sleep(5)
    #
    @allure.title("Create and post new content for all roles")
    @pytest.mark.parametrize(
        "role, message", [
            # ("user", "I'm USER"),
            ("admin", "I'm ADMIN"),
        ]
    )
    def test_create_and_post_new_content_for_all_roles(self, role, message):
        self.login_page.open()
        self.login_page.login_as(role)
        self.home_page.write_post(message)
        self.home_page.post()
        time.sleep(5)

    @allure.title("Create post")
    @pytest.mark.parametrize(
        "role, message", [
            # ("user", "I'm USER"),
            ("admin", "I'm ADMIN"),
        ]
    )
    def test_create_post(self, role, message):
        self.login_page.open()
        self.login_page.login_as(role)
        self.home_page.write_post(message)
        self.home_page.post()
        if role == "admin":
            self.home_page.mark_post_as_admin()
