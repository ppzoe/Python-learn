#导入webdriver
# from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

#创建一个浏览器对象
wb=WebDriver(executable_path="chromedriver")

#浏览器访问指定的URL
wb.execute('get',{'url':'http://www.baidu.com'})

#元素的定位与操作
el=wb.execute('findElement',{
    'using':By.XPATH,
    'value':'//input[@id="kw"]'

})['value']
el._execute('sendKeysToElement',{'text':'可口可乐',
                                'value':''})
ell=wb.execute('findElement',{
    'using':By.XPATH,
    'value':'//input[@id="su"]'
})['value']
ell.execute('clickElement')