class Constants(object):
    MAX_PROJECT_NUMBER_CAN_BE_TESTED = "1000"

    ONE_SECONDS_IN_MILLISECONDS = 1000

    TEST_STRING_FOR_GOOGLE_SEARCH_HAPPY_CASE = "True fit"

    TEST_STRING_FOR_GOOGLE_SEARCH_SAD_CASE_EMPTY_STRING = ""

    TEST_STRING_FOR_GOOGLE_SEARCH_EDGE_CASE_ONE_SPACE = " "
    
    WEBDRIVER_FIREFOX_PATH = "./geckodriver"

    WEBDRIVER_CHROME_PATH = "./chromedriver"

    TEST_GOOGLE_URL = "https://www.google.com"

    TEST_GOOGLE_HOMEPAGE_LOGO_CSS_PATH = "#hplogo"

    TEST_GOOGLE_HOMEPAGE_SEARCH_FIELD_CSS_PATH = "#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input"

    TEST_GOOGLE_HOMEPAGE_SEARCH_BUTTON_CSS_PATH = "#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.VlcLAe > center > input[type=\"submit\"]:nth-child(1)"

    TEST_GOOGLE_HOMEPAGE_SEARCH_BUTTON_NAME = "btnK"
