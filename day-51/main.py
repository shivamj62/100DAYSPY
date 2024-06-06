import time
from selenium import webdriver
from selenium.webdriver.common.by import By


PROMISED_DOWN = 30
PROMISED_UP = 20
TWITTER_EMAIL = "shivam.jaiswal6204@gamil.com"
TWITTER_PASSWORD = "3zMs}T&2Yn&4qQ!"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
    def get_internet_speed(self):

        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        # time.sleep(60)
        # self.up = self.driver.find_element(By.XPATH,value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        # self.down = self.driver.find_element(By.XPATH,value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # print(self.up)
        # print(self.down)
        pass

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()