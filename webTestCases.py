import time, re
import json
import urllib.request
import pytest
from constants import Constants
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver import ActionChains as ac 
from time import sleep
from configparser import SafeConfigParser


@pytest.mark.functional
def test_GoogleHomePage_connectivity():
    url = "https://google.com"
    #driver = webdriver.Firefox(executable_path=Constants.WEBDRIVER_FIREFOX_PATH)
    driver = webdriver.Chrome(executable_path=Constants.WEBDRIVER_CHROME_PATH)
    driver.get(url)

    assert basic(3) ==4

def test_GoogleHomePage_logo_image():
    print('1')

def test_GoogleHomePage_text_field():
    print('2')

def test_GoogleHomePage_search_button():
    print('3')


def basic(x):
    return x+1


if __name__ == "__main__":
    main()