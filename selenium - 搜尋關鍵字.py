from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser= webdriver.Chrome()
browser.get("https://www.google.com")
inputElement = browser.find_element_by_name("q")
inputElement.send_keys("Selenium")
inputElement.submit()
resultLocator = "//a/h3/div"

try:
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located\
                 ((By.XPATH, resultLocator)))
    page1_results = browser.find_elements_by_xpath(resultLocator)

    for item in page1_results:
        print(item.text)
except TimeoutException:
    print('等待逾時！')