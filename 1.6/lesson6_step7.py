from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.XPATH, "//input[@type = 'text']")
    for element in elements:
        element.send_keys("42")
        
    button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()