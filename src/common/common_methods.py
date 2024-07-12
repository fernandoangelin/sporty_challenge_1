from logging import info
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.pages.directory import Directory
from src.pages.streamer import Streamer
from time import sleep

def is_element_in_viewport(browser, element):
    return browser.execute_script(
        "var rect = arguments[0].getBoundingClientRect();"
        "return (rect.top >= 0 && rect.left >= 0 && "
        "rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && "
        "rect.right <= (window.innerWidth || document.documentElement.clientWidth));", element)

def scroll_down(browser, times):
    while times > 0:
        info("Scrolling down countdown: {}".format(times))
        times-=1
        browser.execute_script("window.scrollBy(0, 1000);")
        sleep(1)

def accept_classification_gate(browser):
    wait = WebDriverWait(browser, 5)
    try:
        classification_gate_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Streamer.classification_gate_button_selector))
        )
        if classification_gate_button.is_displayed():
            info("Clicking classification gate button.")
            classification_gate_button.click()
        else:
            info("Classification gate button is not displayed.")
    except TimeoutException:
        info("Classification gate not needed (button not found).")

def delete_cookies_modal(browser):
    try:
        browser.execute_script("document.querySelector('#root > div.Layout-sc-1xcs6mc-0.eTiaZz > div').remove();")
        info("Cookies modal force delete")
    except:
        info("Cookies modal already closed")

def get_first_on_screen_streamer(browser):
    wait = WebDriverWait(browser, 5)
    info("Waiting the loading of the videos")
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, Directory.video_list_selector)))

    info("Getting all videos")
    elements = browser.find_elements(By.CSS_SELECTOR, Directory.video_list_selector)

    for element in elements:
        if element.is_displayed() and is_element_in_viewport(browser, element):
            return element
    else:
        info("No videos were found")
