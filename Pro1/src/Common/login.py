from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
class Login(object):
    def loginsuces(self,username, password):
        # chrome_driver_path = Service()
        chrome_driver_path = Service(os.path.dirname(os.path.abspath('../Common')) + '/Common/chromedriver.exe')
        driver = webdriver.Chrome(service=chrome_driver_path)
        driver.implicitly_wait(1)
        driver.get('http://novel.hctestedu.com/?to=pc')




        driver.find_element(By.CLASS_NAME, 'mr15').click()
        driver.find_element(By.ID, 'txtUName').send_keys(username)
        driver.find_element(By.ID, 'txtPassword').send_keys(password)
        driver.find_element(By.ID, 'btnLogin').click()
        time.sleep(1)
        # driver.refresh()
        result = driver.find_element(By.XPATH,'//*[@id="headerUserInfo"]/span/a[2]').text
        print(result)
        return result


    def loginfailed(self,username, password):
        chrome_driver_path = Service(os.path.dirname(os.path.abspath('../common')) + '/common/chromedriver.exe')
        driver = webdriver.Chrome(service=chrome_driver_path)
        driver.implicitly_wait(1)
        driver.get('http://novel.hctestedu.com/?to=pc')
        driver.find_element(By.CLASS_NAME, 'mr15').click()

        if username is not None:
            driver.find_element(By.ID, 'txtUName').send_keys(username)
        if password is not None:
            driver.find_element(By.ID, 'txtPassword').send_keys(password)

        driver.find_element(By.ID, 'btnLogin').click()
        time.sleep(1)
        faults_text = []

        fault_text = driver.find_element(By.ID, 'LabErr').text
        faults_text.append(fault_text)

        driver.quit()

        for fault_text in faults_text:
            if fault_text != '':
                return fault_text


l = Login()
l.loginsuces(18810209264,123456)