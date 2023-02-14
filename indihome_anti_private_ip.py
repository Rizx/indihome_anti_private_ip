from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
public = ["10"]
while public[0] == "10":
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), chrome_options=chrome_options)
    driver.get("http://192.168.1.1/")
    username = driver.find_elements(By.ID, "Frm_Username")
    password = driver.find_elements(By.ID, "Frm_Password")
    username[0].send_keys("admin")  # ADD USERNAME IN STRING
    password[0].send_keys("Telkomdso123")  # ADD PASSWORD IN STRING
    val_username = username[0].get_attribute('value')
    val_password = password[0].get_attribute('value')
    login = driver.find_elements(By.ID, 'LoginId')
    login[0].click()
    time.sleep(1)

    internetMenu = driver.find_elements(By.ID, 'internet')
    internetMenu[0].click()
    time.sleep(1)

    wanTab = driver.find_elements(By.ID, 'ethWanStatus')
    wanTab[0].click()

    time.sleep(1)
    IP_WAN = driver.find_elements(By.ID,
        "cIPAddress:2")[0].get_attribute('title')
    print(IP_WAN)

    depan = IP_WAN.split(".")
    print(depan[0])
    if depan[0] == "10":
        mgrMenu = driver.find_elements(By.ID, 'mgrAndDiag')
        mgrMenu[0].click()
        time.sleep(1)

        devMgr = driver.find_elements(By.ID, 'devMgr')
        devMgr[0].click()
        time.sleep(1)

        Btn_restart = driver.find_elements(By.ID, 'Btn_restart')
        Btn_restart[0].click()
        time.sleep(1)

        confirmOK = driver.find_elements(By.ID, 'confirmOK')
        confirmOK[0].click()
    else:
        print("Not private IP, skipping")
    time.sleep(30)
