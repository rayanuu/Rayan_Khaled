
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
import math
import pandas as pd
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)


def set_input_value(xpath,value):
    driver.find_element(by=By.XPATH,value=xpath).send_keys(value)

def set_basic_form_infos(title,url,text,body): 
     # set input title
    set_input_value('/html/body/div[2]/div/div[5]/main/div[4]/div[1]/form/div/div[1]/div[1]/div/input',title)
    # set input url
    set_input_value('//*[@id="edit-field-e-resource-url-0-uri"]',url)
    #set input text 
    set_input_value('//*[@id="edit-field-e-resource-url-0-title"]',text)
    # set input body
    iframe = driver.find_element(by=By.TAG_NAME,value="iframe")
    driver.switch_to.frame(iframe)
    set_input_value('/html/body/p',body)
    driver.switch_to.default_content()

    # Login

def portal_scrapper(username,pwd):
    

    login_url = 'https://library-portal.kfupm.edu.sa/en/user/login'
    driver.get(login_url)

    
    try:
        name = driver.find_element(by=By.ID, value="edit-name")
        name.send_keys(username)
        password = driver.find_element(by=By.ID, value="edit-pass")
        password.send_keys(pwd)
        submit = driver.find_element(by=By.ID, value="edit-submit")
        submit.click()
    except NoSuchElementException:
        print("Error")
    # End Login


    #  Enter to resources
    eresources = 'https://library-portal.kfupm.edu.sa/en/node/add/e_resource'
    try:
        driver.get(eresources)

        data = pd.read_csv('data.csv', sep=",",encoding='cp1252',skiprows=1,names=['title','url','text','summary','lang','body','image'])
        for d in data.iterrows():
            title = d[1]['title']
            url = d[1]['url']
            text = d[1]['text']
            summary = d[1]['summary']
            lang = d[1]['lang']
            body = d[1]['body']
            image = dir_path +'/images/'+d[1]['image']
            set_basic_form_infos(text=text,url=url,body=body,title=title)

            submit_Add_media = driver.find_element(by=By.ID, value="edit-field-e-image-open-button")
            submit_Add_media.click()
            
            break


    except NoSuchElementException:
        print('error')
    time.sleep(500)
portal_scrapper("admin_user","5rQkkE25N7necmL")