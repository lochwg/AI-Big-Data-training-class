from selenium import webdriver
import time

url = 'C:\\Users\\user\\Desktop\\chromedriver.exe'
driver = webdriver.Chrome(url)
driver.get("http://www.yahoo.com")
time.sleep(5)
driver.close()
driver.quit()