from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

URl = "https://tinder.com/"
s = Service(YOUR_Chrome_Driver_path)

driver = webdriver.Chrome(service=s)
driver.get(URl)

fb_acount = Your_facebook_login_email
fb_Password = Your_facebook_password



try:
    accept_cookie = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
    accept_cookie.click()
except NoSuchElementException:
    pass

try:
    login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div['
                                          '2]/div[2]/a/div[2]/div[2]')
    login.click()
    print('clicked accept cookie')
    more_options = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/button')
    more_options.click()
except NoSuchElementException:
    pass

time.sleep(5)
try:
    facebook = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]')
    time.sleep(1)
    facebook.click()
    time.sleep(1)
    google_login = driver.window_handles[1]
    driver.switch_to.window(google_login)
except NoSuchElementException:
    pass

try:
    email = driver.find_element(By.XPATH, '//*[@id="email"]')
    email.send_keys(fb_acount)
    time.sleep(1)
    password = driver.find_element(By.XPATH, '//*[@id="pass"]')
    password.send_keys(fb_Password)
    password.send_keys(Keys.ENTER)
    base_window = driver.window_handles[0]
    driver.switch_to.window(base_window)
    print(driver.title)
except NoSuchElementException:
    pass

try:
    time.sleep(1)
    location = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[1]/div[1]')
    location.click()
except NoSuchElementException:
    pass


try:
    for n in range(100):
        time.sleep(1)

        like = driver.find_element(By.XPATH,
                                   '//*[@id="q888578821"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')

        like.click()
except ElementClickInterceptedException:
    try:
        match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
        match_popup.click()
    except NoSuchElementException:
        pass

driver.quit()

