from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import json
import os
import time


def read_data_json():
    script_dir = os.path.dirname(__file__)
    json_path = os.path.join(script_dir, "user.json")
    with open(json_path) as file:
        return json.load(file)


data = read_data_json()

WAIT_TIME = data["wait_time"]

MAX_RETRIES = data["max_retries"]

USERNAME = data["username"]

PASSWORD = data["password"]


def find_element_with_retry(
    driver, by, value, max_retries=MAX_RETRIES, wait_time=WAIT_TIME
):
    retries = 0
    while retries < max_retries:
        try:
            element = driver.find_element(by, value)
            wait = WebDriverWait(driver, wait_time)
            wait.until(lambda d: element.is_displayed())
            return element

        except NoSuchElementException:
            retries += 1
            print(
                f'''Elemento "{value}" não encontrado,
                tentando novamente ({retries}/{max_retries})...'''
            )
            time.sleep(wait_time)
    raise NoSuchElementException(
        f'''Elemento "{value}" não encontrado após
        {max_retries} tentativas. O script foi encerrado.'''
    )


def login():
    try:
        driver = webdriver.Edge()

        driver.maximize_window()

        driver.get("https://www.instagram.com/")

        input_username = find_element_with_retry(
            driver, By.XPATH, '//input[@name="username"]'
        )

        input_username.send_keys(USERNAME)

        input_password = find_element_with_retry(
            driver, By.XPATH, "//input[@name='password']"
        )

        input_password.send_keys(PASSWORD)

        btn_login = find_element_with_retry(
            driver, By.XPATH, '//button[@type="submit"]'
        )

        btn_login.click()

        first_popup = find_element_with_retry(
            driver, By.XPATH, '//div[contains( text(),"Agora não")]'
        )

        first_popup.click()

        second_popup = find_element_with_retry(
            driver, By.XPATH, '//button[contains( text(),"Agora não")]'
        )

        second_popup.click()

        input('Pressione "Enter" para fechar o navegador...')

    except NoSuchElementException as e:
        print(e)

    finally:
        driver.quit()


if __name__ == "__main__":
    login()
