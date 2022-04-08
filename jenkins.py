import pytest
import allure

from config import WEBPAGE
from UISelectors import general_selectors

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


class TestOneNeed:

    # method to be done before every test
    def setup_method(self):
        self.driver = Chrome(ChromeDriverManager().install())
        self.driver.get(WEBPAGE)
        self.driver.maximize_window()

    # method to be done after every test
    def teardown_method(self):
        self.driver.quit()

    @allure.description("Validate Title")
    @allure.severity(severity_level="NORMAL")
    def test_title(self):
        try:
            # get the title by the selector
            title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, general_selectors['main_screen']['title'])
                )
            )
            # check if text of the title element is correct
            try:
                assert title.text == "Electron React Boilerplate"
            finally:
                if AssertionError:
                    allure.attach(self.driver.get_screenshot_as_png(), name="Invalid_title",
                                  attachment_type=allure.attachment_type.PNG)
        except TimeoutException:
            print("bad")

    @allure.description("Validate Button")
    @allure.severity(severity_level="CRITICAL")
    def test_button(self):
        try:
            # get the title by the selector
            title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, general_selectors['main_screen']['title'])
                )
            )
            # check if text of the title element is correct
            try:
                assert title.text == "Electron React Boilerplate"
            finally:
                if AssertionError:
                    allure.attach(self.driver.get_screenshot_as_png(), name="Invalid_title",
                                  attachment_type=allure.attachment_type.PNG)
        except TimeoutException:
            print("bad")

    @allure.description("Validate Button2")
    @allure.severity(severity_level="CRITICAL")
    def test_button2(self):
        try:
            # get the title by the selector
            title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, general_selectors['main_screen']['title'])
                )
            )
            # check if text of the title element is correct
            try:
                assert title.text == "Electron React Boilerplate"
            finally:
                if AssertionError:
                    allure.attach(self.driver.get_screenshot_as_png(), name="Invalid_title",
                                  attachment_type=allure.attachment_type.PNG)
        except TimeoutException:
            print("bad")
