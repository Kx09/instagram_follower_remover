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

def enterPasword(driver,username,password):#enters given password

    # Find username and password fields and submit button
    username_input = driver.find_element("name", "username")
    password_input = driver.find_element("name","password")

    login_button = driver.find_element("xpath","//button[@type='submit']")

    # Enter your login information

    username_input.send_keys(username)
    password_input.send_keys(password)

    # Click the login button
    login_button.click()
    time.sleep(3)


def removeOuterloop(driver,profiles_keep):#outer loop goes through 

    time.sleep(2)
    profile_button = driver.find_elements("class name","x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft")

    for button in profile_button:
        #print(button.text)
        if button.text == "Profile":
            button.click()

    
    time.sleep(2)




    class_name = convert_class_name("x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd")
    followers_n_following = driver.find_elements("class name",class_name)

    print(followers_n_following)


    once = True 

    for buts in followers_n_following:
        if once == True:
             remove_followers(buts,driver,profiles_keep)
             once = False


        else:
             remove_following(buts,driver,profiles_keep)


                
        
     
def remove_following(buts,driver,profiles_keep):
            
            #waits for button click 
            buts.click()
            time.sleep(2)

            #finds every button for 
            prof_class = convert_class_name("_ap3a _aaco _aacw _aacx _aad7 _aade")
            followings = driver.find_elements("class name",prof_class)
            time.sleep(3)

                

            name_removes = convert_class_name("_ap3a _aaco _aacw _aad6 _aade")
            removes = driver.find_elements("class name",name_removes)

            time.sleep(2)


            counter = 0 

            find_num_followers = convert_class_name("html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs")
            nums = driver.find_elements("class name",find_num_followers)


            num_followers = int(nums[2].text)
            print(f"The number of following is {num_followers}")

            

            
            for i in range(num_followers):
                if followings[i].text in profiles_keep:
                        i = i + 1
                        time.sleep(2)
                        continue
                else:
                    removes[i].click()
                    time.sleep(1)
                    clsname = convert_class_name("_a9-- _ap36 _a9-_")
                    unfollow_button = driver.find_elements("class name",clsname)
                    unfollow_button.click()
                    
                    del removes[i]
                    time.sleep(2)

                                        
            cross = driver.find_element("class name","_abm0")
            cross.click()

                       




def remove_followers(buts,driver,profiles_keep):
            
            profile_postition = 0
            buts.click()
            time.sleep(2)

            prof_class = convert_class_name("_ap3a _aaco _aacw _aacx _aad7 _aade")
            profiles = driver.find_elements("class name",prof_class)

            name_removes = convert_class_name("x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x16n37ib x1uhb9sk x1plvlek xryxfnj x1c4vz4f xs83m0k x1q0g3np xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1")
            removes = driver.find_elements("class name",name_removes)

    

            print(removes)

            
            counter = 0
           
            find_num_followers = convert_class_name("html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs")
            nums = driver.find_elements("class name",find_num_followers)


            num_followers = int(nums[1].text)
            print(f"The number of following is {num_followers}")

            

            for i in range(num_followers):
                print(profiles[counter].text)
                if profiles[counter].text in profiles_keep:
                        counter = counter + 1
                        continue
                else:
                    removes[counter].click()
                    del removes[counter]
                    try:
                        remove_button = driver.find_element("class name","_a9--._ap36._a9-_")
                        remove_button.click()
                        time.sleep(1)
                    except:
                         print("Could not find remove button, possible delay")
                    counter = counter + 1
                

                        
            cross = driver.find_element("class name","_abm0")
            cross.click()
            once = False            


def convert_class_name(string):
    following_string = string
    class_name_clean= following_string.replace(" ",".")

    return class_name_clean


def main():
    driver = OpenBrowser()
    username = "maplechaipod"
    password = "aoanazareen123"
    enterPasword(driver,username,password)



    profiles_keep = ["krem808s"]
    removeOuterloop(driver,profiles_keep)
    print("The bot has been completed, profiles removed")
    driver.quit()



main()
