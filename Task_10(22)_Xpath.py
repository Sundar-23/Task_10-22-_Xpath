
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver import ActionChains
import time

# Maximize window
opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")


chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

# input web page
driver.implicitly_wait(5)
driver.get("https://www.instagram.com/guviofficial/")

# Finding Xpath for followers
followers = driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[2]/span").text
print("followers: ", followers)

# Finding Xpath for following
following = driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[3]/span").text
print("following: ",following)


#closing the window
driver.quit()