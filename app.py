from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os
import time
import subprocess
if (os.name =='posix') : path = subprocess.run(["whereis","firefox.geckodriver"],capture_output=True,text=True,check=True).stdout.strip().split(":")[1].strip().split()[0]
if (os.name =='nt') : path = str(os.path.dirname(os.path.realpath(__file__) )) + '/geckodriverWin.exe' 



service = Service(path)
options = Options()
options.add_argument("--headless")
browser  = webdriver.Firefox(service = service,options=options)

#login page url
wifi_auth = browser.get('http://detectportal.firefox.com/canonical.html')
# store credentials
load_dotenv()
username=os.getenv("auth_user")
password=os.getenv("auth_password")

time.sleep(2)

#Fill the details
auth_user_element = browser.find_element(By.ID,'auth_user')	
auth_password_element = browser.find_element(By.ID,'auth_pass')
submit_button_element = browser.find_element(By.ID,'login')


auth_user_element.clear()
auth_password_element.clear()
auth_user_element.send_keys(username)
auth_password_element.send_keys(password)

submit_button_element.click()	
