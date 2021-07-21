import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "cleverqazi"
USERNAME = "YOUR INSTAGRAM USERNAME"
PASSWORD = "YOUR PASSWORD"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(5)
        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get("https://www.instagram.com/" + SIMILAR_ACCOUNT)

        time.sleep(5)
        followers_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/'
                                                           'li[2]/a')
        followers_link.click()

        time.sleep(5)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height
            # of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(5)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


follow = InstaFollower()
follow.login()
follow.find_followers()
follow.follow()
