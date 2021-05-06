import time

from selenium import webdriver

from github_userinfo import username, password


class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Firefox()
        self.username = username
        self.password = password
        self.follower = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath('//*[@id="login_field"]').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[12]').click()

    def getFollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        item = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        for i in item:
            self.follower.append(i.find_element_by_css_selector(".link-gray.pl-1").text)

        while True:
            links = self.browser.find_element_by_class_name("BtnGroup").find_elements_by_tag_name("a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)

                    item = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
                    for i in item:
                        self.follower.append(i.find_element_by_css_selector(".link-gray.pl-1").text)
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        item = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
                        for i in item:
                            self.follower.append(i.find_element_by_css_selector(".link-gray.pl-1").text)
                    else:
                        continue


github = Github(username,password)
github.signIn()
github.follower()
print(github.follower)