from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Firefox()
    link = "https://SunInJuly.github.io/execute_script.html"
    driver.get(link)

    x = driver.find_element_by_id("input_value").text
    answer_input = driver.find_element_by_id("answer")
    button = driver.find_element_by_tag_name("button")
    driver.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)

    answer_input.send_keys(calc(x))

    cheak = driver.find_element_by_id("robotCheckbox")
    cheak.click()

    radio = driver.find_element_by_css_selector("[for='robotsRule']")
    radio.click()
    
    button.click()

finally:
    time.sleep(15)
    driver.quit()
    