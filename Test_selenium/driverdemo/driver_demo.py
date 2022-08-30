from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://music.163.com/')
driver.implicitly_wait(3)
# 打开登录界面
driver.find_element(By.XPATH, "//*[text()='登录']/..").click()
# 显示等待 (名称，最大时间，每次扫描时间）until定位需要等待的元素 （）中填写函数；   until_not （）内显示为假（等待到此元素消失为止）；message=‘’可以设置报错提醒语句
WebDriverWait(driver, 6, 0.5).until(lambda el: driver.find_element(By.XPATH, "//*[text()='选择其他登录模式']/."),
                                     message="异常没有定位成功")
# 跳转到账号登录
sleep(3)
element = driver.find_element(By.XPATH, "//*[text()='选择其他登录模式']/.")
element.click()
# 同意用户协议
sleep(3)
driver.find_element(By.ID, 'j-official-terms').click()
# 跳转到填写密码
driver.find_element(By.XPATH, "//*[text()='手机号登录']/..").click()
# 选着密码登录
driver.find_element(By.XPATH, "//*[@class='_1D0ldyLa']/a").click()
# 输入手机号码
driver.find_element(By.XPATH, "//*[@class='_1aXkUzRt']/input").send_keys('15124401578')
# 输入密码
driver.find_element(By.XPATH, "//*[@class='cWbL7Ab3']/input").send_keys('000asd000asd')
# 点击登录
driver.find_element(By.XPATH, "//*[@class='tan2MIhq']").click()
# 退出
sleep(10)
driver.quit()
