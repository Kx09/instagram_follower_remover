"""
go to instagram, login

"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time 




def OpenBrowser():#Opens browser(Firefox) and returns driver 
    geckodriver_path = r'C:\Program Files\Gekodriver'  # Update this path
    service = Service(geckodriver_path)
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com")
    time.sleep(2)

    return driver 



def enterPasword(driver):#enters given password

    # Find username and password fields and submit button
    username_input = driver.find_element("name", "username")
    password_input = driver.find_element("name","password")

    login_button = driver.find_element("xpath","//button[@type='submit']")

    # Enter your login information

    username_input.send_keys("kevenanderson66")
    password_input.send_keys("instagram@909")

    # Click the login button
    login_button.click()
    time.sleep(3)


def findprofile(driver):
    profile_button = driver.find_element("xpath", "//button[contains(text(), 'Profile')]")
    profile_button.click()
    time.sleep(2)

    followers_butt = driver.find_element("xpath", "//button[contains(text(), 'Followers')]")
    followers_butt.click()
    time.sleep(2)

    removes = driver.find_elements("xpath", "//button[contains(text(), 'Remove')]")
    print(removes)




driver = OpenBrowser()
enterPasword(driver)
findprofile(driver)

