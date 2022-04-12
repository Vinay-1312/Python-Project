from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
Chrom_driver_path = "F:\Vinay\chromedriver.exe"
driver = webdriver.Chrome(Chrom_driver_path)




class Instagram:
  def __init__(self,driver):
      self.driver = driver
      self.driver.get("https://www.instagram.com/accounts/login")
      
  def login_page(self,UserName,password):
      username_field = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
      username_field.send_keys(UserName)
      password_field = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
      password_field.send_keys(password)  
      password_field.send_keys(Keys.ENTER)
  def search(self,search_string):
      search_field = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
      search_field.send_keys(search_string)
      time.sleep(2)
      search_field.send_keys(Keys.ENTER)
      search_field.send_keys(Keys.ENTER)
  def followers_list(self):
      follower_list_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
      follower_list_button.click()
      time.sleep(5)
      self.driver.find_elements(By.CSS_SELECTOR,"._7UhW9")
  /#html/body/div[6]/div/div/div/div[2]/ul/div
  def follow(self):
      all_buttons = self.driver.find_elements_by_css_selector("li button")
      for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

insta = Instagram(driver)
time.sleep(5)
insta.login_page("xxyz91248@gmail.com",os.environ['insta_pass'])
time.sleep(5)
insta.search("ChelseaFC")
time.sleep(5)
insta.followers_list()
time.sleep(5)
insta.follow()
#//*[@id="loginForm"]/div/div[1]/div/label/input

#//*[@id="f219394beb0f2bc"]/button/div

#//*[@id="fce9c3d2d83c2"]/button/div


#'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button'
#'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div'
#sqdOP  L3NKy   y3zKF     

#