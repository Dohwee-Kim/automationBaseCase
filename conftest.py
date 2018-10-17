import pytest
from constants import Constants
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,WebDriverException
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture(params=["chrome","firefox"],scope="class")
def driver_init(request):
    '''
    Returns a webDriver instance and close after each test classes 
    '''
    if request.param == "chrome":
    	try: 
    		webDriverHandler = webdriver.Chrome(executable_path=Constants.WEBDRIVER_CHROME_PATH)
    	except WebDriverException: 
    		print ("ERROR: Failed to start driver at " + Constants.WEBDRIVER_CHROME_PATH)

    elif request.param == "firefox":
    	try: 
    		webDriverHandler = webdriver.Firefox(executable_path=Constants.WEBDRIVER_FIREFOX_PATH)
    	except WebDriverException: 
    		print ("ERROR: Failed to start driver at " + Constants.WEBDRIVER_FIREFOX_PATH)

    else:
    	raise ValueError
    	print ("Please pass one of the following argument (supported web driver) : chrome , firefox ")

    webDriverHandler.maximize_window()
    request.cls.driver = webDriverHandler

    yield webDriverHandler
    webDriverHandler.close()
    