import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def web_browser():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(executable_path=r'/tests/chromedriver', options=chrome_options)
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()

