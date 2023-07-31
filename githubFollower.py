from selenium import webdriver
from selenium.webdriver.common.by import By
from githubUserInfo import username,password
import time


driver = webdriver.Chrome()
url = "https://github.com/"
driver.get(url)
driver.maximize_window()
signIn = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div/a")
signIn.click()
time.sleep(2)
usernameInput = driver.find_element(By.ID, "login_field")
passwordInput = driver.find_element(By.ID, "password")
usernameInput.send_keys(username)
passwordInput.send_keys(password)
signInButton = driver.find_element(By.NAME, "commit")
signInButton.click()
time.sleep(2)
url = "https://github.com/username"
driver.get(url)
time.sleep(2)
followersButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div/div/div[1]/div/div/div[3]/div[2]/div[3]/div/a[1]")
followersButton.click()
time.sleep(2)
followers = driver.find_elements(By.CSS_SELECTOR, 'div.d-table-cell.col-9.v-align-top.pr-3 > a > span.f4.Link--primary')
for follower in followers:
    print(follower.text)
driver.close()