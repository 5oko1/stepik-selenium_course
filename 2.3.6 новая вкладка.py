from selenium import webdriver
import math
import time 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    start_url = "http://suninjuly.github.io/redirect_accept.html"
    driver.get(start_url)

    btn1 = driver.find_element_by_tag_name("button")
    btn1.click()

    window2 = driver.window_handles[1]
    driver.switch_to.window(window2)

    x = driver.find_element_by_id("input_value").text
    answer_input = driver.find_element_by_id("answer")
    answer_input.send_keys(calc(x))

    button = driver.find_element_by_css_selector("button")
    button.click()

    answer = driver.switch_to.alert
    print(answer.text.split()[-1])

finally:
    time.sleep(5)
    driver.quit()
    


