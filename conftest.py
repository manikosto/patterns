import os

import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def set_options():
    if os.environ["BROWSER"] == "chrome":
        options = webdriver.ChromeOptions()
    elif os.environ["BROWSER"] == "firefox":
        options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    return options

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    if os.environ["BROWSER"] == "chrome":
        driver = webdriver.Chrome(options=set_options())
    elif os.environ["BROWSER"] == "firefox":
        driver = webdriver.Firefox(options=set_options())
    request.cls.driver = driver
    yield driver
    driver.quit()
