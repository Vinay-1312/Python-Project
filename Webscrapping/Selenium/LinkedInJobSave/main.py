import requests 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
Chrom_driver_path = "F:\Vinay\chromedriver.exe"
driver = webdriver.Chrome(Chrom_driver_path)
#driver.get("https://www.amazon.com/dp/B0956KYCPS/ref=sspa_dk_detail_0?pd_rd_i=B0956KYCPS&pd_rd_w=Z4r5i&pf_rd_p=b9951ce4-3bd8-4b04-9123-0fda35d6155e&pd_rd_wg=TEHVu&pf_rd_r=YXBKPZGSKKYDAFMP7RDC&pd_rd_r=69da9803-689d-4484-a29d-58fbc64ceb7c&s=kitchen&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFSSUhCV1A2T0VJRUgmZW5jcnlwdGVkSWQ9QTEwMjY5NjExOTRYWUtBSVZFMFpSJmVuY3J5cHRlZEFkSWQ9QTAwMjY0NTMyWDJJQThNWURKOUU2JndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1")

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2990767883&distance=25&f_AL=true&geoId=103671728&keywords=python&location=Pune%2C%20Maharashtra%2C%20India&sortBy=R")


signin = driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[2]')
signin.click()

time.sleep(10)
username = driver.find_element(By.NAME,"session_key")
username.send_keys("vinaysld123@gmail.com")
password = driver.find_element(By.NAME,"session_password")
password.send_keys(os.environ['linkedIn_pass'])

signin_button = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
signin_button.click()


resultSet = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul")
#options = resultSet.find_elements_by_class_name("jobs-search-results__list-item")
all_listings = driver.find_elements(By.CSS_SELECTOR,".job-card-list__title")
c = 0
for option in all_listings:
   
    option.click()
  
    time.sleep(10)
    div_save = driver.find_element(By.CSS_SELECTOR ,".jobs-save-button")
    
    div_save.click()
#driver.quit()


#jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view