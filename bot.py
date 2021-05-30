import time
from selenium import webdriver
from time import sleep
from secrets import pw
from selenium.webdriver.common.keys import Keys
from random import randint

class Bot():

    links = []

    comments = [
        'Great post', 'Awesome!', 'Great Work'
    ]
    def __init__(self):
        # mention your username here , you can mention your password here as well but its better to create an extra python file to store the password.
        # and import that password 
        self.login('your username',pw)
        self.like_comment_by_hashtag('programming','coding')
    
    # this is a function where the selenium gets login 
    
    def login(self, username, password):
        self.driver = webdriver.Chrome('paste the driver path here')
        self.driver.get('https://instagram.com/')
        time.sleep(3)
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        time.sleep(2)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click() #This helps to remove the notnow botton
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click() #This helps to remove the notnow botton
    
    # this is a function where the program search the content or post through #tags 
    
    def like_comment_by_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        links = self.driver.find_elements_by_tag_name('a')
    
    #filters the link of the post or content
    
        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(10):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)
            # like
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(5)

            # does the comment on the post by it self choosing it from above
            
            self.driver.find_element_by_class_name('RxpZH').click() 
            sleep(1)
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,2)])
            sleep(1)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
def main():
    while True:
        my_bot = Bot()
        sleep(60) #prgramme runs after a minute  

if __name__ == '__main__':
    main()
