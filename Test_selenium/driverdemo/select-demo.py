# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
# 导入 ActionChains 类
'''
模拟手机浏览器开启
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'}) # 模拟iPhone X浏览
driver = webdriver.Chrome(options=options)
driver.get('http://m.baidu.com')
'''
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(3)
bg_config = driver.find_element(By.XPATH, "//*[@id='s-usersetting-top']")
ActionChains(driver).move_to_element(bg_config).perform()
driver.find_element(By.XPATH, "//*[@id='s-user-setting-menu']/div/a[1]").click()
# 不同页面跳转需要时间，设置等待时间
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='se-setting-3']/span[2]/span").click()
# 第 2 项 text 为“每页显示 20 条”
driver.quit()
