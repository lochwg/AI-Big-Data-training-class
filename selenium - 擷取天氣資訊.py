from selenium import webdriver
import time

chrome_path = "C:\\Users\\user\\Desktop\\chromedriver.exe"
web = webdriver.Chrome(chrome_path)

web.get('http://www.cwb.gov.tw/V7/')
web.set_window_position(0,0)
web.set_window_size(1680,1280)
time.sleep(5)

web.find_element_by_link_text('天氣').click()
web.find_element_by_link_text('最新天氣').click()
time.sleep(5)

web.close()