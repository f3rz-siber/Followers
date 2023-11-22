from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT = "ACCOUNT"
USERNAME = "putriayundaeva"
PASSWORD = "evayundaputri"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(10)

        name = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        name.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        button = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        button.click()
echo $PATH
echo 'export PATH=$PATH:/path/to/driver' >> ~/.bash_profile
source ~/.bash_profile
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(7)
        scroll = self.driver.find_element(by=By.CLASS_NAME, value='_aano')

        for i in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll)
            time.sleep(5)

    def follow(self):
        follow_button = self.driver.find_elements(by=By.CSS_SELECTOR,
                                                  value='._aano div div div div div div div div button')
        # print("Number of buttons found:", len(follow_button))
        for i in follow_button:
            try:
                i.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                annuler = self.driver.find_element(by=By.XPATH, value='/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                annuler.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
