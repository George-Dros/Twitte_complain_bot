from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import  Keys
import time

PROMISED_DOWN = "your promised download speed from provider"
PROMISED_UP = "your promised upload speed from provider"
chrome_driver_path = "your chrome driver path"
TWITTER_EMAIL = "twitter email"
TWITTER_PASSWORD = "twitter pass"
speed_test_URL = "https://www.speedtest.net/"
twitter_URL = "https://www.twitter.com/"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        s = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(speed_test_URL)
        time.sleep(3)

        accept_button = self.driver.find_element("id", "onetrust-accept-btn-handler")
        time.sleep(3)
        accept_button.click()

        go_button = self.driver.find_element("xpath", '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element("xpath", "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.up = self.driver.find_element("xpath", "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text

    def tweet_at_provider(self):
        self.driver.get(twitter_URL)
        time.sleep(3)

        log_in_button = self.driver.find_element("xpath", '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span')
        log_in_button.click()
        time.sleep(2)

        input = self.driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        input.send_keys(TWITTER_EMAIL)
        input.send_keys(Keys.ENTER)

        time.sleep(2)

        password = self.driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(2)

        tweet = self.driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down} download/ {self.up} upload when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up???")
        tweet_button = self.driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        self.driver.quit()


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()