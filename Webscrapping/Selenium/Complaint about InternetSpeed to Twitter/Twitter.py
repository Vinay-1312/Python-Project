# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:41:12 2022

@author: DELL
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
Chrom_driver_path = "F:\Vinay\chromedriver.exe"

driver = webdriver.Chrome(Chrom_driver_path)
#driver.get("https://www.amazon.com/dp/B0956KYCPS/ref=sspa_dk_detail_0?pd_rd_i=B0956KYCPS&pd_rd_w=Z4r5i&pf_rd_p=b9951ce4-3bd8-4b04-9123-0fda35d6155e&pd_rd_wg=TEHVu&pf_rd_r=YXBKPZGSKKYDAFMP7RDC&pd_rd_r=69da9803-689d-4484-a29d-58fbc64ceb7c&s=kitchen&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFSSUhCV1A2T0VJRUgmZW5jcnlwdGVkSWQ9QTEwMjY5NjExOTRYWUtBSVZFMFpSJmVuY3J5cHRlZEFkSWQ9QTAwMjY0NTMyWDJJQThNWURKOUU2JndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1")

driver.get("https://www.speedtest.net/")

go_button = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go_button.click()
time.sleep(60)
download_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

ds = download_speed.text
us = upload_speed.text
driver.get("https://twitter.com/login")

#login = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
#login.click()
driver.implicitly_wait(10)
time.sleep(5)
input_text = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
input_text.send_keys("xyzxyz40687853")

signin_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
signin_button.click()
time.sleep(5)

password_text = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_text.send_keys(os.environ['twitter_password'])
time.sleep(3)
password_text.send_keys(Keys.ENTER)
#login_button = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
#login_button.click()

time.sleep(5)
driver.implicitly_wait(10)

tweet_text = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
time.sleep(5)
driver.implicitly_wait(50)
tweet_text.click()
tweet_text.send_keys("Hi Your internet download speed is "+ds + " and upload speed is "+ us)
     
time.sleep(5)

driver.implicitly_wait(10)

tweet_button = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
tweet_button.click()