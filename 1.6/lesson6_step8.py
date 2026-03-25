from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/find_xpath_form")
    
    input1 = browser.find_element(By.XPATH, "//input[@name = 'first_name']")
    input1.send_keys("Danil")
    input2 = browser.find_element(By.XPATH, "//input[@name = 'last_name']")
    input2.send_keys("Marchenko")
    input3 = browser.find_element(By.XPATH, "//input[@class = 'form-control city']")
    input3.send_keys("Vladivostok")
    input4 = browser.find_element(By.XPATH, "//input[@id= 'country']")
    input4.send_keys("Russia")
    
    button = browser.find_element(By.XPATH, "//button[@type= 'submit']")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()