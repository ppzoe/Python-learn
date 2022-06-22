import time
from selenium import webdriver
# 创建浏览器对象
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# 跳转到指定URL
driver.get('http://www.baidu.com')


div_list = driver.find_elements(By.XPATH, '//*[@id="scroller"]/div[1]/div')
for div in div_list:
    div.find_element(By.XPATH, "")