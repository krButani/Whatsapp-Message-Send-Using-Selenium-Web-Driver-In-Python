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

#driver = webdriver.Chrome(os.getcwd()+'/chromedriver_win32/chromedriver.exe',chrome_options=chrome_options)
driver = webdriver.Chrome(os.getcwd()+'/chromedriver.exe',chrome_options=chrome_options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
mobile="8460304360"
driver.get("https://api.whatsapp.com/send?phone=91"+mobile)
x_arg = '//a[@title="Share on WhatsApp"]'
btn = wait.until(EC.presence_of_element_located((
				By.XPATH, x_arg)))
btn.click()
msg="hii"
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"][@dir="ltr"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(1):
    input_box.send_keys(msg + Keys.RETURN)
    time.sleep(1)