from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "test.txt")

try:
    driver = webdriver.Firefox()
    driver.get("http://suninjuly.github.io/file_input.html")

    firstname = driver.find_element_by_name("firstname")
    firstname.send_keys("Egor")
    lastname = driver.find_element_by_name("lastname")
    lastname.send_keys("Sever")
    email = driver.find_element_by_name("email")
    email.send_keys("Sever")
    file_ = driver.find_element_by_name("file")
    file_.send_keys(file_path)

    btn = driver.find_element_by_tag_name('button')
    btn.click()

finally:
    time.sleep(5)
    driver.close()