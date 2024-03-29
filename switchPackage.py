import os
import time
import selenium
from LoginToJobbliss import *
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from PIL import Image
from Screenshot import *
from uploadDocument import *


USERNAME = 'anesuchiodza@yahoo.com'
PASSWORD = 'testCase123_'

TIMEOUT=10
fscreenshot = Screenshot.Screenshot()

logging.basicConfig(filename='LoginSeq_Log.txt', level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode='w')
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
#options.add_argument("--headless")
options.add_argument("--kiosk")

browser = webdriver.Chrome(executable_path=CM().install(), options=options)
#LoginToCompany
browser.get(
    'https://alpha.jobbliss.com/signin')



#time.sleep(20)
print("[Info] - Logging in process in progress...")
# emailAddress
user_element = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.NAME, 'email')))

user_element.send_keys(USERNAME)

#time.sleep(5)


# PassWord
passWed = browser.find_element(By.XPATH, '//input[@id="password"]')

#pass_element.send_keys(PASSWORD)
passWed.send_keys(PASSWORD)

login_button = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div/span/form/div[1]/div/button')))

time.sleep(0.4)

login_button.click()

time.sleep(10)

browser.get('https://alpha.jobbliss.com/dashboard')

try:
    #check if we have actually got in on the site since you can not access dashboard without logging in. Element to be located is the dashbord text "Dashboard"
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[1]/ul/li/span[2]'))
        # Take a screenshot of the Page and store it for analysis.
    
    )
    profilePackage = WebDriverWait(browser, TIMEOUT).until(
    EC.presence_of_element_located((
        By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/nav/div/div/div/div[3]/div[1]/div[1]')))

    profilePackage.click()
    #pricing Management path

    pricingManagement = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/nav/div/div/div/div[3]/div[2]/div[3]/span')))

    pricingManagement.click()



    clickPackage = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/main/div[2]/div/div[2]/div/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/button')))

    clickPackage.click()
    time.sleep(3)

    clickYes = WebDriverWait(browser, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/form/div[2]/div[1]/div/button')))

    clickYes.click()


    # Take a screenshot of the Page and store it for analysis.
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='SuccessFullCreation.png')
    time.sleep(3)
    screenshot = Image.open('SuccessFullCreation.png')
    get_url = browser.current_url
    print("You are now on :"+str(get_url))
    print("You have successfully Created and completed setting up your profile")
    # screenshot.show()
    image = fscreenshot.full_Screenshot(browser, save_path=r'.', image_name='CompanyLoggedIn.png')
    time.sleep(3)

    header = ['Test Name', 'State']

    #data
    data = ['Company Login', 'Passed']

    with open('AutomationQA_Summary.csv','a',encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        writer.writerow(data)

        time.sleep(3)
    print("Logged In As a Company/Admin Successfully")

finally:
    #browser.quit()  
    print('script done running.. on to the next, please check results to understand status of test..')  

# clickPackage Button




