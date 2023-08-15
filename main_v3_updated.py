from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import requests
import random
import time


login_dict = {'email':'password'}

artist_list = ['artist_name']

telegram_id = 'telegram_d'


def user_agent():
    options = Options()
    ua = UserAgent()
    user_agent = ua.random
    print(user_agent)
    options.add_argument(f'--user-agent={user_agent}')

def web_login(driver,email,password):
    # Open Ticketmaster Italy website
    driver.get("https://shop.ticketmaster.it/accountLogin.html")

    sleep(3)
    driver.maximize_window()
    accept_cookie = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    accept_cookie.click()
    sleep(1)

    # Find the username and password input fields, and fill them with your credentials
    username_field = driver.find_element(By.XPATH, "//input[@name='login']")
    username_field.send_keys(email)
    sleep(randint(2,5))

    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys(password)


    checkmark = driver.find_element(By.XPATH, "//span[@class='checkmark']")
    checkmark.click()
    sleep(randint(2,5))

    do_login = driver.find_element(By.XPATH, "//input[@id='doLogin']")
    do_login.click()


def send_to_telegram(message):

    apiToken = '6304206327:AAFi8RPGjQOqBlwxHpXjIKXtRpl77uIM1n8'
    chatID = telegram_id
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

def buy_ticket(event,driver):
    driver.get(event)
    sleep(10)
    try:
        ul_element = driver.find_element(By.XPATH, '//select[@onclick="abledBtnBuy();"]')
        mx = ul_element.get_attribute("qtqtymax")
        ul_element.click()
        max_opt = '//option[@value="'+str(mx)+'"]'
        options = ul_element.find_element(By.XPATH, max_opt )
        options.click()
        ul_element.click()

        time.sleep(random.uniform(2, 6))
        e_Ticket = driver.find_element(By.XPATH, '//*[@id="ico_TM_eTicket"]/span')
        e_Ticket.click()
        time.sleep(random.uniform(2, 6))
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='reCAPTCHA']"))
        re_captchabox = driver.find_element(By.XPATH, "//span[@id='recaptcha-anchor']")
        time.sleep(random.uniform(2, 6))
        re_captchabox.click()
        time.sleep(random.uniform(2, 6))
        driver.switch_to.default_content()
        buy_button  = driver.find_element(By.XPATH, '//*[@id="btnBuy"]')
        buy_button.click()
        sleep(5)

        for i in range(2,int(mx)+2):
            fr_name = '/html/body/div[1]/div[2]/div/form[2]/table/tbody[2]/tr['+str(i)+']/td/div/div/div/div[1]/input'
            lst_name = '/html/body/div[1]/div[2]/div/form[2]/table/tbody[2]/tr['+str(i)+']/td/div/div/div/div[2]/input'
            sleep(2)
            fr_name_inp = driver.find_element(By.XPATH, fr_name)
            sleep(1)
            fr_name_inp.send_keys('Andrea')
            sleep(2)
            lst_name_inp = driver.find_element(By.XPATH, lst_name)
            sleep(1)
            lst_name_inp.send_keys('Di Bari')

        
        confirm_btn = driver.find_element(By.XPATH, '//input[@name="doSaveRegistrant"]')
        confirm_btn.click()
        sleep(10)

        for j in range(1,4):
            sleep(2)

            try:
                xp = '//*[@id="accountTermsForm"]/div/div['+str(j)+']/label/span'
                element = driver.find_element(By.XPATH, xp)
                try:
                    inp = '//*[@id="accountTermsForm"]/div/div['+str(j)+']/label/input'
                    inp.get_attribute("checked")
                    continue
                except:
                    xp = '//*[@id="accountTermsForm"]/div/div['+str(j)+']/label/span'
                    element = driver.find_element(By.XPATH, xp)
                    element.click()
            except:
                continue
            

        sleep(3)

        fnl_btn = driver.find_element(By.XPATH, "//input[@value='Conferma']")
        fnl_btn.click()

        sleep(3)

        current_url = driver.current_url
        message = "Hello I'm your ticketmaster bot. Event ticket are available! Open your cart and grab your ticket now. Here is the url " + str(current_url)
        send_to_telegram(message)
        print("Message has been sended your for ticket's")
    except:
        print("Ticket's are not availble")


def main(): 
    while True:
        for email,password in login_dict.items():

            user_agent()
            # Start a Chrome browser session
            driver = webdriver.Chrome()
            driver.maximize_window()
            time.sleep(3)
            web_login(driver,email,password)

            sleep(8)

            for i in range(0,len(artist_list)):

                driver.get('https://shop.ticketmaster.it/eventi-futuri.html')
                search_bar = driver.find_element(By.XPATH, "//input[@class='search']")
                sleep(3)
                search_bar.send_keys(artist_list[i])
                search_bar.send_keys(Keys.RETURN)

                main_event_list = []
                event_list = []

                for j in range(1,30):
                    try:    
                        ele = "//*[@id='pageInfo']/div[2]/div[2]/ul/li["+str(j)+"]/div[1]/div/div[3]/a"
                        ul_element = driver.find_element(By.XPATH, ele)
                        main_event_list.append(ul_element.get_attribute("href"))

                    except:
                        try:
                            if len(event_list) == 0:
                                ele = '//*[@id="pageInfo"]/div[2]/div/div[2]/div[2]/ul/li[1]/div[1]/div/div[3]/a'
                                ul_element = driver.find_element(By.XPATH, ele)
                                event_list.append(ul_element.get_attribute("href"))
                                main_event_list.append(ul_element.get_attribute("href"))
                        except:
                            break
                
                sleep(3)
                for event in main_event_list:
                    try:
                        buy_ticket(event,driver)
                        sleep(120)
                    except: 
                        print("Ticket's are not availble for this event :(")

            driver.quit()
            sleep(3)
            
if __name__ == "__main__":
    main()



