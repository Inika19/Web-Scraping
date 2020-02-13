from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time
from random import randint,randrange

path = '/Users/inika/Desktop/notebooks/Web Scraping/Selenium/chromedriver' # path to webdriver
driver = webdriver.Chrome(path)

# set login credentials,server and channel names here
username = "sample_username_here"
password = "sample_password_here"
server = "servername"

driver.get('https://discordapp.com')
time.sleep(1)

try:
    driver.find_element_by_link_text("Login").click()
    tb = driver.find_elements_by_tag_name("input")

    tb[0].send_keys(username)
    tb[1].send_keys(password)
    tb[1].submit()
    
except NoSuchElementException:
        driver.find_element_by_link_text("Open").click() 

time.sleep(10)
anchors = driver.find_elements_by_tag_name("a")
for a in anchors:
    try:
        if a.get_attribute("aria-label")==server:
            a.click()
    except StaleElementReferenceException:
        break

time.sleep(1)
channels = driver.find_elements_by_class_name("name-3_Dsmg")
for c in channels:
    if c.text == 'spam':
        c.click()

t = driver.find_element_by_xpath('//div[@aria-label = "Message #spam"]')

p1 = 'pls '
p2 = 'pet '
p = p1+p2
petcom = ['feed','wash','play','pat']
commands = [p+pc for pc in petcom]
commands.append(p1+'beg')
commands.append(p1+'gamble 1')
commands.append(p1+'slots 1')
commands.append('pls pm')
meme_categories = ['d','e','n','s','r']

while True:
    try:
        w = randrange(10,600)
        i = randint(0,len(commands)-1)
        t.send_keys(commands[i])
        t.send_keys(Keys.RETURN)
        if commands[i]=='pls pm':
            t.send_keys(meme_categories[randint(0,4)])
            t.send_keys(Keys.RETURN)
        time.sleep(w)
                            
    except StaleElementReferenceException:
        continue