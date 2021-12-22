import os

from selenium import webdriver
from selenium.webdriver.common.by import By

from Duoling import constants as const

print("You might have to run script twice incase of error\n")
username = input("\nWhats Your Username: ")
password = input("Whats Your Password: ")
title2 = input("Enter Title: ")
message = input("Enter message: ")

class Duo(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\Trevo\OneDrive\Desktop\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += r"C:\Users\Trevo\OneDrive\Desktop\SeleniumDrivers"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Duo, self).__init__(options=options)  # Gets rid of the errors in the terminal
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def fist_page(self):
        self.get(const.BASE_URL)




    def login(self):
        log = self.find_element(By.CLASS_NAME, '_13HXc')
        log.click()

        user_name = self.find_element(By.CSS_SELECTOR, '[data-test="email-input"]')
        pass_word = self.find_element(By.CSS_SELECTOR, '[data-test="password-input"]')

        user_name.send_keys(username)

        pass_word.send_keys(password)

        log2 = self.find_element(By.CSS_SELECTOR, '[data-test="register-button"]')
        log2.click()

        # Takes you to the forum page

    def discuss(self):
        self.implicitly_wait(5)
        discuss_button = self.find_element(By.CSS_SELECTOR, '[data-test="discussion-nav"]')
        discuss_button.click()


        select = self.find_element(By.CLASS_NAME, "_3zsRU")
        select.click()

    def new_message(self):
        self.implicitly_wait(2)
        new_post = self.find_element(By.CSS_SELECTOR,
                                     '[style="background: rgb(120, 200, 0); border-color: rgb(88, 167, 0); color: rgb(255, 255, 253);"]')
        new_post.click()

        self.implicitly_wait(2)
        new_post1 = self.find_element(By.CSS_SELECTOR,
                                      '[style="background: rgb(120, 200, 0); border-color: rgb(88, 167, 0); color: rgb(255, 255, 253);"]')
        new_post1.click()

        title = self.find_element(By.CSS_SELECTOR, '[placeholder="Type your post title"]')
        title.send_keys(title2)

        post = self.find_element(By.CSS_SELECTOR, '[placeholder="Type your post"]')
        post.send_keys(message)

    # Post the message and checks

    def final(self):
        post_final = self.find_element(By.CSS_SELECTOR,
                                       '[style="background: rgb(28, 176, 246); border-color: rgb(24, 153, 214); color: rgb(255, 255, 253);"]')

        try:

            post_final.click()
            print('\nposted')

        except:
            print("\nfailed to post")
