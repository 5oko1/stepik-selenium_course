from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

try:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    start_url = "http://suninjuly.github.io/selects1.html"

    driver.get(start_url)

    num1 = int(driver.find_element_by_id("num1").text)
    num2 = int(driver.find_element_by_id("num2").text)

    selector = Select(driver.find_element_by_id("dropdown"))
    selector.select_by_value(str(num1+num2))

    button = driver.find_element_by_css_selector("button")
    button.click()

finally:
    time.sleep(15)
    driver.quit()
    


