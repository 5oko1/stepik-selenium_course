from selenium import webdriver
import math
import time 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    start_url = "http://suninjuly.github.io/math.html"

    driver.get(start_url)

    x = driver.find_element_by_id("input_value").text
    answer_input = driver.find_element_by_id("answer")
    answer_input.send_keys(calc(x))

    cheak = driver.find_element_by_id("robotCheckbox")
    cheak.click()

    radio = driver.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    button = driver.find_element_by_css_selector("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    driver.close()
    


