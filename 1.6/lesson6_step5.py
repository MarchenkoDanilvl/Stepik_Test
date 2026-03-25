from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/find_link_text")

try:
    link = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link1 = browser.find_element(By.LINK_TEXT, link)
    link1.click()
    
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Danil")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Marchenko")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Vladivostok")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()
    
finally:
    time.sleep(30)
    browser.quit()

