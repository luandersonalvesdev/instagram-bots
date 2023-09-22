from selenium import webdriver
from selenium.webdriver.common.by import By
import json


def login():
    with open("user.json") as file:
        json_file = json.load(file)

        USERNAME = json_file["username"]
        PASSWORD = json_file["password"]

    TIMER = 5

    driver = webdriver.Edge()

    driver.maximize_window()

    driver.get("https://www.instagram.com/")

    driver.implicitly_wait(TIMER)

    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(USERNAME)

    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(PASSWORD)

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    driver.implicitly_wait(TIMER * 3)

    driver.find_element(By.XPATH, '//div[contains( text(),"Agora não")]').click()

    driver.find_element(By.XPATH, '//button[contains( text(),"Agora não")]').click()

    input('Pressione "Enter" para fechar o navegador...')

    driver.quit()


if __name__ == "__main__":
    login()
