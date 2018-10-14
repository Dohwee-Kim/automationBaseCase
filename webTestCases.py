import time, re
import json
import urllib.request
import constants
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver import ActionChains as ac 
from time import sleep


@pytest.mark.functional
def test_GoogleHomePage_connectivity():
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