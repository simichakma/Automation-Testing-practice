import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()
