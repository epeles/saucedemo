from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

SAUCEDO_USERNAME = "standard_user"
SAUCEDO_PASSWORD = "secret_sauce"
FIRST_NAME = "Eitan"
LAST_NAME = "Peles"
POSTAL_CODE = "22222-010"