from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time                     
driver = webdriver.Chrome("C:/Users/Microsoft/Downloads/chromedriver_win32/chromedriver.exe")  #change this
driver.get("http://www.instagram.com")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
username.send_keys("username") #change
password.clear()
password.send_keys("password") #change
Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(2)
notNowButton = WebDriverWait(driver, 15).until(
lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
notNowButton.click()
driver.get("https://www.instagram.com/username/")  #change the username in the url to your username
time.sleep(2)
links = driver.find_elements(By.TAG_NAME, "a")
driver.execute_script("arguments[0].click();",links[2])
time.sleep(3)
for i in range(5):
    time.sleep(3)
    links = driver.find_elements(By.TAG_NAME, "a")
    driver.execute_script("arguments[0].click();",links[2])
    time.sleep(3)
    all_buttons = driver.find_elements_by_tag_name("button")
    unfollow_buttons = [btn for btn in all_buttons if btn.text == "Following"]
    time.sleep(2)
    for i in range(len(unfollow_buttons)):
        time.sleep(2)
        driver.execute_script("arguments[0].click();",unfollow_buttons[i])
        time.sleep(2)
        all_buttons = driver.find_elements_by_tag_name("button")
        final_button = [btn for btn in all_buttons if btn.text == "Unfollow"]
        driver.execute_script("arguments[0].click();",final_button[0])
        
    driver.refresh()
