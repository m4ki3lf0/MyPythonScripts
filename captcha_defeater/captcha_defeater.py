import re
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

api_key = "YOUR 2captcha API KEY"


def selenium_get(url):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    chrome_options = Options()

    return driver


def validate_captcha(driver):
    time.sleep(5)  # wait for the page to load
    # Exemple on https://google.com/recaptcha/api2/demo
    # With driver
    data_sitekey = driver.find_element(
        "xpath", '//*[@id="recaptcha-demo"]'
    ).get_attribute("data-sitekey")
    # OR with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data_sitekey1 = soup.find("div", {"id": "recaptcha-demo"}).get("data-sitekey")
    # OR with regex
    data_sitekey2 = re.search(r'data-sitekey="(.+?)"', driver.page_source).group(1)

    form = {
        "method": "userrecaptcha",
        "googlekey": data_sitekey,  # or data_sitekey1 or data_sitekey2
        "key": api_key,
        "pageurl": "https://google.com/recaptcha/api2/demo",
        "json": 1,
    }
    # get the token from 2captcha
    response = requests.post("http://2captcha.com/in.php", data=form)
    request_id = response.json()["request"]

    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"
    # wait for the captcha to be solved
    while True:
        response = requests.get(url)
        if response.json()["status"] == 1:
            captcha_token = response.json()["request"]
            js = f"document.getElementById('g-recaptcha-response').innerHTML = '{captcha_token}';"
            driver.execute_script(js)
            break
        else:
            print("Waiting for token")
            time.sleep(5)


def main():
    driver = selenium_get("https://google.com/recaptcha/api2/demo")
    validate_captcha(driver)
    # Now you juste have to accomplish the action you want
    # Here you can see how to input some text in an input field
    # driver.find_element('xpath','//*[@id="input1"]').send_keys('Whatever the form asks for')
    # Exemple on https://google.com/recaptcha/api2/demo click the submit button
    driver.find_element("xpath", '//*[@id="recaptcha-demo-submit"]').click()
    # OR with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    soup.find("button", {"id": "recaptcha-demo-submit"}).click()


if __name__ == "__main__":
    main()
