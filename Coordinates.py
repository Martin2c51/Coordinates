from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

def Coordinates(a):
    
    driver = webdriver.Chrome("C:/Users/dema8017/Desktop/Coordinates/chromedriver.exe")
    driver.get('https://plus.codes/7697V2PV+V7F')
    
    sub=driver.find_element_by_css_selector('.sprite-bg')
    time.sleep(2)
    sub.click()
    time.sleep(2)
    n=len(a)
    coor=[]
    window=driver.find_element_by_css_selector('#search-input')
    time.sleep(2)
    window.send_keys(a[0])
    time.sleep(2)
    window.send_keys(Keys.RETURN)
    time.sleep(2)
    cor=driver.find_element_by_css_selector('#placecard-details')
    cor=cor.text
    try:
        coor.append(cor)
        cor2 = cor
    except:
        coor.append("")
    time.sleep(2)
    window.clear()
    if n>1:
        for i in range(1,n):
            time.sleep(2)
            window=driver.find_element_by_css_selector('#search-input')
            window.send_keys(a[i])
            time.sleep(2)
            window.send_keys(Keys.RETURN)
            time.sleep(2)
            cor=driver.find_element_by_css_selector('#placecard-details')
            cor=cor.text
            try:
                if cor2==cor:
                    cor = cor + " Check"
                    coor.append(cor)
                else:
                    coor.append(cor)
                    cor2 = cor
            except:
                coor.append("")
            window.clear()
            time.sleep(2)
        driver.quit()
        return(coor)
    else:
        driver.quit()
        return(coor)
        


    






    
            
