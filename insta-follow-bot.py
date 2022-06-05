from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time                     
driver = webdriver.Chrome("C:/Users/rites/OneDrive/Documents/chromedriver_win32/chromedriver.exe") #replace this with your path to driver
driver.get("http://www.instagram.com")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
username.send_keys("your username") #change this
password.clear()
password.send_keys("your password")#change this
Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(2)
notNowButton = WebDriverWait(driver, 15).until(
lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
notNowButton.click()
driver.get("https://www.instagram.com/explore/people/")
for i in range(10):
    time.sleep(3)
    follow_buttons = driver.find_elements_by_tag_name("button")
    time.sleep(2)
    for i in range(len(follow_buttons)):
        time.sleep(1)
        driver.execute_script("arguments[0].click();",follow_buttons[i])
    driver.refresh()
