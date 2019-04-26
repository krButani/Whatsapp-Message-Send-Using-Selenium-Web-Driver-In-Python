from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import csv
import os


from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("disable-popup-blocking")


driver = webdriver.Chrome(os.getcwd()+'/chromedriver',options=chrome_options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)


print('==============================================================')

wtime = input('Enter Wait Time')
ttime = int(wtime)

print('==============================================================')
	
msg = input('Enter Message: ')

print('First Login Whatsapp')



def main(no):
    mobile = no.lstrip('91')
    mobile = mobile.lstrip("0")
    print(mobile)
    print('-------------------------------------------------------------------------')

    driver.get("https://api.whatsapp.com/send?phone=91"+mobile)
    x_arg = '//a[@title="Share on WhatsApp"]'
    btn = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    for i in range(100):
        try:
            btn.click()
        except:
            try:
                x_arg2 = '//div[contains(text(), "Phone number shared via url is invalid.")]'
                btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                    By.XPATH, x_arg2)))
                print(mobile + ' is Not Register in Whatsapp.')
            except:
                inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"][@dir="ltr"]'
                input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath)))
                for i in range(1):
                    input_box.send_keys(msg + Keys.RETURN)
                    time.sleep(1)
                try:
                    #WebDriverWait(driver, ttime).until(EC.alert_is_present(),
                    #        'Timed out waiting for PA creation ' +
                    #        'confirmation popup to appear.')
                    #popup = driver.switch_to.alert
                    #popup.accept()
                    driver.switchTo().alert().dismiss(); 
                except:
                    print('No alert')
            break
        time.sleep(1)


c=1
with open('wp.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        if c <= 20:
            tmp=row[2]
            k=tmp.split(",")
            #print(k)
            no1=''
            no2=''
            if len(k) == 2:
                no1=k[0].strip()
                no2=k[1].strip()
            else:
                no1=k[0].strip()
            c=c+1
            if len(no1) ==  10:
                try:
                    main(no1)
                except:
                    print(no1+" is Give Error")
            
            if len(no2) ==  10:
                try:
                    main(no2)
                except:
                    print(no1+" is Give Error")
