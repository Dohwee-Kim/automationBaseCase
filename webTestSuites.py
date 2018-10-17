import time, re
import json
import urllib.request
import pytest
from constants import Constants
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains as ac 
from time import sleep


@pytest.mark.functional
def test_GoogleHomePage_logo_image():
    url = Constants.TEST_GOOGLE_URL
    driver_Chrome = webdriver.Chrome(executable_path=Constants.WEBDRIVER_CHROME_PATH)
    driver_Chrome.maximize_window()

    driver_Chrome.get(url)
    
    driver_Chrome.implicitly_wait(3) #seconds 
    element_google_logo = driver_Chrome.find_element_by_css_selector(Constants.TEST_GOOGLE_HOMEPAGE_LOGO_CSS_PATH)

    driver_Chrome.close()

@pytest.mark.functional
def test_GoogleHomePage_search_text_field():
    url = Constants.TEST_GOOGLE_URL
    driver_Chrome = webdriver.Chrome(executable_path=Constants.WEBDRIVER_CHROME_PATH)
    driver_Chrome.get(url)
    driver_Chrome.maximize_window()

    driver_Chrome.implicitly_wait(3) #seconds
    element_google_search_field = driver_Chrome.find_element_by_css_selector(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_FIELD_CSS_PATH)

    driver_Chrome.close()

@pytest.mark.functional
def test_GoogleHomePage_search_button():
    url = Constants.TEST_GOOGLE_URL
    driver_Chrome = webdriver.Chrome(executable_path=Constants.WEBDRIVER_CHROME_PATH)
    driver_Chrome.implicitly_wait(3) #seconds
    driver_Chrome.get(url)
    driver_Chrome.maximize_window()

    driver_Chrome.implicitly_wait(3) #seconds
    element_google_search_button = driver_Chrome.find_element_by_name(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_BUTTON_NAME)

    driver_Chrome.close()

@pytest.mark.functional
def test_GoogleHomePage_search_field_validity_test_with_a_valid_textinput():
    url = Constants.TEST_GOOGLE_URL
    driver_Chrome = webdriver.Chrome(executable_path=Constants.WEBDRIVER_CHROME_PATH)
    driver_Chrome.get(url)
    driver_Chrome.maximize_window()
    driver_Chrome.implicitly_wait(3) #seconds

    element_google_search_field = driver_Chrome.find_element_by_css_selector(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_FIELD_CSS_PATH)

    element_google_search_field.send_keys(Constants.TEST_STRING_FOR_GOOGLE_SEARCH_HAPPY_CASE)

    element_google_search_button = driver_Chrome.find_element_by_name(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_BUTTON_NAME)

    element_google_search_button.submit()

    driver_Chrome.implicitly_wait(3) #seconds

    driver_Chrome.close()

@pytest.mark.functional
def test_GoogleHomePage_search_field_validity_test_without_a_textinput():
    url = Constants.TEST_GOOGLE_URL
    driver_Chrome = webdriver.Chrome(executable_path=Constants.WEBDRIVER_CHROME_PATH)
    driver_Chrome.get(url)
    driver_Chrome.maximize_window()
    driver_Chrome.implicitly_wait(3) #seconds

    element_google_search_field = driver_Chrome.find_element_by_css_selector(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_FIELD_CSS_PATH)

    element_google_search_field.send_keys(Constants.TEST_STRING_FOR_GOOGLE_SEARCH_SAD_CASE_EMPTY_STRING)

    element_google_search_button = driver_Chrome.find_element_by_name(Constants.TEST_GOOGLE_HOMEPAGE_SEARCH_BUTTON_NAME)

    element_google_search_button.submit()

    driver_Chrome.implicitly_wait(3) #seconds

    assert True == element_google_search_button.is_enabled()

    driver_Chrome.close()

