from logging import info
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.common.common_methods import accept_classification_gate
from src.common.common_methods import delete_cookies_modal
from src.common.common_methods import get_first_on_screen_streamer
from src.common.common_methods import scroll_down
from src.pages.homepage import Homepage
from src.setup.setup_browser import browser
from time import sleep

def test_select_streamer_mobile_view(browser):
    wait = WebDriverWait(browser, 5)
    info("Accessing https://www.twitch.tv/")
    url = "https://www.twitch.tv/"
    browser.get(url)
    sleep(5)
    info("Asserting Twitch in the browser title")
    assert "Twitch" in browser.title

    reject_cookies_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Homepage.reject_cookies_button_selector))
    )
    info("Clicking reject cookies")
    reject_cookies_button.click()

    # This is a workaround to close the cookies modal
    delete_cookies_modal(browser)

    search_icon = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Homepage.search_icon_selector))
    )
    info("Clicking search icon")
    search_icon.click()

    search_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Homepage.search_input_selector))
    )
    info("Typing StarCraft II into the search input")
    search_input.send_keys("StarCraft II")

    game = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, Homepage.game_selector))
    )
    # This wait is to make sure the correct item is selected
    sleep(1)
    info("Clicking searched game")
    game.click()

    # This wait is to make sure the correct item is loaded
    sleep(1)
    info("Asserting StarCraft II in the browser title")
    assert "StarCraft II" in browser.title

    info("Scrolling down...")
    scroll_down(browser, 2)

    first_video_visible = get_first_on_screen_streamer(browser)
    first_video_visible.click()

    info("Accepting classification gate if displayed")
    accept_classification_gate(browser)

    info("Taking a screenshot")
    browser.save_screenshot("screenshot.png")
    sleep(5)
