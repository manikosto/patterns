import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    caps = DesiredCapabilities.CHROME.copy()
    caps['browserVersion'] = '117.0'

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )
    # driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()