import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestStepic:
    message = ""
    @pytest.mark.parametrize('id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_guest_should_see_login_link(self, browser, id):
        link = f"https://stepik.org/lesson/{id}/step/1/"
        browser.get(link)

        browser.implicitly_wait(10)

        button1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "ember458")))
        button1.click()

        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys("")

        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys("")

        button2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sign-form__btn")))
        button2.click()

        time.sleep(1)
        answer = math.log(int(time.time()))
        input3 = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        input3.send_keys(answer)

        time.sleep(1)
        button3 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        button3.click()

        message_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints')))
        self.message = message_element.text

        if self.message != "Correct!":
            self.message += f" {self.message}"
            print(self.message)

        assert self.message == "Correct!", f"Expected message to be different from 'Correct!', but got: {self.message}"
