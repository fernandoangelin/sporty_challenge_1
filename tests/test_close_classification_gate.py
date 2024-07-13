from logging import info
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.common.common_methods import accept_classification_gate
from src.common.common_methods import delete_cookies_modal
from src.pages.homepage import Homepage
from src.setup.setup_browser import browser
from time import sleep

def test_close_classification_gate_mobile_view(browser):
    wait = WebDriverWait(browser, 5)
    url = "https://www.twitch.tv/leva2k"
    browser.get(url)
    # wait to make sure the page is loaded
    sleep(2)

    reject_cookies_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Homepage.reject_cookies_button_selector))
    )
    reject_cookies_button.click()

    # This is a workaround to close the cookies modal
    delete_cookies_modal(browser)

    # wait to make sure the page is loaded
    sleep (2)
    info("Accepting classification gate if displayed")
    accept_classification_gate(browser)
    # wait to make sure the page is loaded
    sleep(2)
