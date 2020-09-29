# Basic Automation Suite
This Python script with Pytest is for simple webpage loading test
=======
Basic case for Python automation 

This is a basic test automation examples for Google Homepage written in Python 3.7 using Selenium WebDriver and Pytest.
If you use a Anaconda, setting up an clean environment with a specific version of Python 3.7 is recommended. It might work with other 3.7.x versions but have not tested. 

```
conda create -n <env_name> python=3.7
```

Requirements:
```
atomicwrites    1.2.1    
attrs           18.2.0   
certifi         2018.8.24
chardet         3.0.4    
idna            2.7      
more-itertools  4.3.0    
pip             10.0.1   
pluggy          0.7.1    
py              1.7.0    
pytest          3.8.2    
pytest-html     1.19.0   
pytest-metadata 1.7.0    
selenium        3.14.1   
setuptools      40.4.3   
six             1.11.0   
urllib3         1.23     
wheel           0.32.1  
```

#Chrome and Gecko drivers!!
Repository includes Mac OS 64 GeckoDriver for FireFox and ChromeDriver for Chrome. If you want to run this tests on different OS system, Please replace driver files.

Here are download links:
```
Chrome Driver : https://chromedriver.storage.googleapis.com/index.html?path=2.43/
Gecko Driver :https://github.com/mozilla/geckodriver/releases
```

You will need to install above the requirements first using following command in command line.
This will generate report.html file for tests result in HTML format on the test source folder. 
```
pip install -r requirements.txt --ignore-installed
```

To run use the following command run from the cloned directory:
```
pytest -v testCasesGoogle.py --html=report.html

if you want to run specific test:
pytest -v testCasesGoogle.py::<pytest marked class name>

ex) pytest -v testCasesGoogle.py::Test_Google_Pages

if you want to run tests with specific web browser:
pytest -v -k <'chrome'|'firefox'> testCasesGoogle.py --html=report.html 

```

Important Source Code Breakdown:
```
confest.py 
  - Configuration for pre-tests loading. Using fixture, this will load appropriate web-browser
 at the beginning of the tests(class), and close it at the end of the tests(class)

testCasesGoogle.py
  - pytest is run against these test files. 
  - It contains tests cases by class, and methods named start with test_*.
  - This uses webDriver instance from fixture (request driver in confest.py), test variables from constants.py 
  
constants.py
  - class object contains defined string, numbers, and variables for test cases. 
  
report.html 
  - Generated test report by --html=<filename> option.
```
