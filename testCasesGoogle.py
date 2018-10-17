import time, re
import pytest
from constants import Constants
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains as ac 
from time import sleep

@pytest.mark.usefixtures("driver_init")
class TestBase():
    pass

@pytest.mark.usefixtures("driver_init")
class Test_Google_Pages():
    def test_Google_page_logo_image(self):
        self.driver.get(Constants.TEST_GOOGLE_URL)

        wait= WebDriverWait(self.driver, 3)

        element_google_logo = self.driver.find_element_by_css_selector(Constants.TEST_GOOGLE_HOMEPAGE_LOGO_CSS_PATH)

    def test_Google_page_search_text_field(self):
        self.driver.get(Constants.TEST_GOOGLE_URL)

        wait= WebDriverWait(self.driver, 3)

        element_google_search_field = self.driver.find_element_by_css_selector(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_FIELD_CSS_PATH)

    def test_Google_page_search_button(self):
        self.driver.get(Constants.TEST_GOOGLE_URL)

        wait= WebDriverWait(self.driver, 3)

        element_google_search_button = self.driver.find_element_by_name(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_BUTTON_NAME)

    def test_Google_page_search_field_validity_test_valid_input(self):
        self.driver.get(Constants.TEST_GOOGLE_URL)

        wait= WebDriverWait(self.driver, 3)

        element_google_search_field = self.driver.find_element_by_css_selector(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_FIELD_CSS_PATH)

        element_google_search_field.send_keys(Constants.TEST_STRING_FOR_GOOGLE_SEARCH_HAPPY_CASE)

        element_google_search_button = self.driver.find_element_by_name(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_BUTTON_NAME)

        element_google_search_button.submit()

    def test_Google_page_search_field_validity_test_invalid_input(self):
        self.driver.get(Constants.TEST_GOOGLE_URL)

        wait= WebDriverWait(self.driver, 3)

        element_google_search_field = self.driver.find_element_by_css_selector(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_FIELD_CSS_PATH)

        element_google_search_field.send_keys(Constants.TEST_STRING_FOR_GOOGLE_SEARCH_SAD_CASE_EMPTY_STRING)

        element_google_search_button = self.driver.find_element_by_name(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_BUTTON_NAME)

        element_google_search_button.submit()

        wait= WebDriverWait(self.driver, 3)

        assert True == element_google_search_button.is_enabled()