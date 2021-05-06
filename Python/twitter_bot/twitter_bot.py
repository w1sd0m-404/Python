import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from twitter_info import username, password


class Main:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.web = webdriver.Firefox()

    def signIn(self):
        self.web.get("https://twitter.com/login")
        time.sleep(2)
        usernameInput = self.web.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        passwordInput = self.web.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        self.web.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div').click()
        time.sleep(2)

    def search(self,hashtag):
        searchInput = self.web.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        loopCounter = 0
        last_height = self.web.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > 5:
                break
            self.web.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.web.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter+=1

        count = 1
        list = self.web.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
        for i in list:
            print("*"*10)
            print(count,i.text)
            count+=1

twitter = Main(username,password)
#login
twitter.signIn()
#twitter.search("mercedes")