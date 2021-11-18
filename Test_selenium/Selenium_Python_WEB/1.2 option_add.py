#导入webdriver模块
from selenium import webdriver
#导入强制等待
from time import sleep
#去黄条（浏览器标签下帮助条）
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
#去头模式开启，隐藏执行程序不显示
# option.add_argument('headless')
#创建一个浏览器对象(去黄条，去头模式启用option设置)
driver=webdriver.Chrome(chrome_options=option)
#访问指定的URL
driver.get('https://www.baidu.com/')
#打印网站名称
print(driver.title)
#查找需要操作的元素
we_input=driver.find_element_by_id('kw')#we=webelement
#对元素进行输入操作
we_input.send_keys('王牌对王牌')
#点击百度一下按钮，执行本次搜索操作
we_button=driver.find_element_by_id('su')
we_button.click()
#WebDriver是服务代理，当自动化结束时，需要记得释放资源
sleep(5)
driver.quit()
#close关闭标签；quit关闭浏览器，释放进程
