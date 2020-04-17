from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Firefox()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    price = driver.find_element_by_id("price")
    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = driver.find_element_by_id("book")
    button.click()

    x = driver.find_element_by_id("input_value").text
    answer = driver.find_element_by_tag_name("input")
    driver.execute_script("return arguments[0].scrollIntoView({block: 'center'});", answer)
    answer.send_keys(calc(x))

    sumbit_btn = driver.find_element_by_id("solve").click()

    alert = driver.switch_to.alert
    print(alert.text.split()[-1])

finally:
    driver.quit()