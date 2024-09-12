import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    answer = math.log(abs(12 * math.sin(int(x))))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")

    option2.click()


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
