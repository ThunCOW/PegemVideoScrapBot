from pickle import TRUE
from turtle import goto
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import urllib.request
import os

import time

def main():
    opt = webdriver.ChromeOptions()
    opt.add_extension('C:\\Users\MONSTER\\Visual Studio Code\\Python\\python3105\\PegemKPSScrapper\\pegemscrp\\downloaderApp.crx')

    s = Service('C:\\Users\MONSTER\\Visual Studio Code\\Python\\python3105\\PegemKPSScrapper\\pegemscrp\\chromedriver.exe')

    driver_main = webdriver.Chrome(service=s, options=opt)

    url_extension = 'chrome-extension://eaicplkoeceoelookkiaeekhodehdhde/data/dialog/index.html'
    url_pegem = 'https://dijital.pegemkampus.com/MobileApp/BookPortal/BookDetails?bookId=326'
    url_pegem_login = 'https://dijital.pegemkampus.com/giris?returnUrl=%27/portal%27'


    driver_main.get(url_pegem_login)
    driver_main.set_window_size(1920, 1080)

    # login pegem
    time.sleep(1)
    driver_main.find_element("xpath", '//*[@id="UserName"]').send_keys('ekremtunc1998@gmail.com')
    driver_main.find_element("xpath", '//*[@id="Password"]').send_keys('ekrem1998')
    driver_main.find_element("xpath", '//*[@id="form0"]/div[5]/div/button').click()

    # go to activation page
    time.sleep(1)
    driver_main.find_element("xpath", '//*[@id="kt_header_menu"]/ul/li[2]/a').click()
    # go to activation details
    time.sleep(1)
    driver_main.find_element("xpath", '//*[@id="activationCodeList"]/table/tbody/tr/td[7]/span/a').click()
    # select the book
    time.sleep(1)
    driver_main.find_element("xpath", '//*[@id="packageDetails"]/div/div/div[2]/div[1]/div[2]/a').click()

    """
    # extend list
    time.sleep(5)
    driver_main.find_element(By.XPATH, '//*[@id="headingOne_1274"]').click()
    time.sleep(5)
    parent = driver_main.find_element(By.XPATH, '//*[@id="collapseOne_1274"]')
    testList = parent.find_elements(By.TAG_NAME, "a")
    print(len(testList))
    
    testNumber = 1
    GetTest(driver_main, testNumber, testList, 5)
    """
    
    time.sleep(5)
    driver_main.find_element(By.XPATH, '//*[@id="headingOne_1274"]').click()
    time.sleep(5)
    testList = driver_main.find_element(By.XPATH, '//*[@id="collapseOne_1274"]').find_elements(By.TAG_NAME, 'a')
    print(len(testList))

    testNumber = 46
    GetTest(driver_main, testNumber, testList, 5)
    
    #for
    
    """
    for i in range(len(testList)):
        i = testNumber
        if not os.path.exists('C:\\Users\\MONSTER\\Visual Studio Code\\Python\\python3105\\PegemKPSScrapper\\pegemscrp\\KPSS_cografya\\Test %s' %testNumber):
            os.makedirs('C:\\Users\\MONSTER\\Visual Studio Code\\Python\\python3105\\PegemKPSScrapper\\pegemscrp\\KPSS_cografya\\Test %s' %testNumber)
        testList[i-1].click()
        GetVideos(driver_main, testNumber)
        time.sleep(5)
        testNumber = testNumber + 1

    for test in testList:
        if not os.path.exists('C:\\Users\\MONSTER\\Visual Studio Code\\Python\\python3105\\PegemKPSScrapper\\pegemscrp\\KPSS_cografya\\Test %s' %testNumber):
            os.makedirs('C:\\Users\\MONSTER\\Visual Studio Code\\Python\\python3105\\PegemKPSScrapper\\pegemscrp\\KPSS_cografya\\Test %s' %testNumber)
        test.click()
        GetVideos(driver_main, testNumber)
        time.sleep(5)
        testNumber = testNumber + 1
    """
        
def GetTest(driver_main, testNumber, testList, errorTolarance):
    if(testNumber <= len(testList)):
        if(errorTolarance > 0):
            for i in range(len(testList)):
                try:
                    i = testNumber
                    if not os.path.exists('C:\\Users\\MONSTER\\Visual Studio Code\\Python\\python3105\\PegemKPSScrapper\\pegemscrp\\KPSS_cografya\\Test %s' %testNumber):
                        os.makedirs('C:\\Users\\MONSTER\\Visual Studio Code\\Python\\python3105\\PegemKPSScrapper\\pegemscrp\\KPSS_cografya\\Test %s' %testNumber)
                    testList[i-1].click()
                    GetVideos(driver_main, testNumber)
                    time.sleep(5)
                    testNumber = testNumber + 1
                except:
                    print('Test %s''de hata yasandi' %testNumber)
                    time.sleep(10)
                    GetTest(driver_main, testNumber, testList, errorTolarance - 1)
        else:
            print('Test %s hatali oldugundan atlandi.' %testNumber)
            GetTest(driver_main, testNumber + 1, testList, 5)

def GetVideos(driver_main, testNumber):
    # test is open, get the link of questions
    time.sleep(5)
    parent = driver_main.find_element(By.CLASS_NAME, 'questionanswerbox')
    questions = parent.find_elements(By.TAG_NAME, "a")

    # go through questions and download them one by one
    order = 0
    for question in questions:
        errorTolerance = 5
        order = order + 1
        Video(driver_main, testNumber, question, order, errorTolerance)
            
                
def Video(driver_main, testNumber, question, order, errorTolarance):
    if(errorTolarance > 0):
        try:
            question.click()
            time.sleep(5)
            driver_main.find_element(By.CLASS_NAME, 'js-player')
            video_link = driver_main.find_element(By.XPATH, '//*[@id="player"]/source').get_attribute('src')
            
            urllib.request.urlretrieve(video_link, 'C:\\Users\\MONSTER\\Visual Studio Code\\Python\\python3105\\PegemKPSScrapper\\pegemscrp\\KPSS_cografya\\Test %s' %testNumber + '\\%s. Soru.mp4' %order)
            time.sleep(2)
            errorTolarance = 0
        except:
            time.sleep(10)
            Video(driver_main, testNumber, question, order, errorTolarance - 1)
    else:
        print('Test %s ' %testNumber + 'Soru %s hatali oldugundan yuklenemedi.' %order)

if __name__ == "__main__":
    main()