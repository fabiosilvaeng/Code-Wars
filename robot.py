# Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# import schedule

# Configurações WebDriver
options = Options()
#options.add_argument('--headless') #enabled in productions
# options.add_argument('--no-sandbox')  # enabled in productions
# options.add_argument("--disable-setuid-sandbox")  # enabled in productions
options.add_argument("window-size=1920x1080")  # enabled in productions
# options.add_argument("--disable-dev-shm-usage")  # enabled in productions
options.add_argument("start-maximized")  # enabled in productions
options.add_argument("--log-level=3")  # enabled in productions

chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

data ={
    'url':'https://outlook.live.com/owa/',
    'email':'fjas96@hotmail.com',
    'senha':'Fa*33525226',
}


chrome.get(data['url'])

click_login = chrome.find_element(By.XPATH,'/html/body/header/div/aside/div/nav/ul/li[2]/a')
if click_login:
    click_login.click()

dig_email = chrome.find_element(By.XPATH,'//*[@id="i0116"]')
if dig_email:
    for i in data['email']:
        dig_email.send_keys(i)
        sleep (0.1)

click_prox_email = chrome.find_element(By.XPATH,'//*[@id="idSIButton9"]')
if click_prox_email:
    click_prox_email.click()

dig_senha = chrome.find_element(By.XPATH,'//input[@type="password"]')
if dig_senha:
        dig_senha.send_keys(data['senha'])
        sleep (0.1)
sleep(2)
enter_email = chrome.find_element(By.XPATH,'//*[@id="idSIButton9"]')
if enter_email:
    enter_email.click()

try:
    keep_login = chrome.find_element(By.XPATH,'//*[@id="idBtn_Back"]')
    if keep_login:
        keep_login.click()
except:
    pass

       
sleep (1000)