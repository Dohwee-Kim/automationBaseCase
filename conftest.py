import pytest
from constants import Constants
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,WebDriverException
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(scope="class")
def driver_init(request):
    '''
    Returns a webDriver instance and close after each test classes 
    '''
    try: 
    	webDriverHandler = webdriver.Chrome(executable_path=Constants.WEBDRIVER_CHROME_PATH)
    except WebDriverException: 
    	print ("ERROR: Failed to start driver at " + Constants.WEBDRIVER_CHROME_PATH)
    webDriverHandler.maximize_window()
    request.cls.driver = webDriverHandler

    yield webDriverHandler
    webDriverHandler.close()
    