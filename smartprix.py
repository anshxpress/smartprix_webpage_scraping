from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.smartprix.com/mobiles")
time.sleep(0.5)

driver.find_element(by= By.XPATH, value='//*[@id="app"]/main/aside/div/div[6]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by= By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()  
time.sleep(1)

link2 = driver.find_element(by = By.XPATH, value='/html/body/div[1]/header/section[2]/a[5]')
link2.click()
