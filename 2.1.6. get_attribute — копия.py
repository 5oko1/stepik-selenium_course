from selenium import webdriver
import math
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    start_url = "http://suninjuly.github.io/get_attribute.html"

    driver.get(start_url)

    x = driver.find_element_by_css_selector("img").get_attribute("valuex")
    answer_input = driver.find_element_by_id("answer")
    answer_input.send_keys(calc(x))

    cheak = driver.find_element_by_id("robotCheckbox")
    cheak.click()

    radio = driver.find_element_by_id("robotsRule")
    radio.click()

    button = driver.find_element_by_css_selector("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    driver.quit()
    


