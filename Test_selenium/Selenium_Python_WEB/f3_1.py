#导包
from selenium import webdriver
from time import sleep
class TestKeyWords(object):
    #初始化
    def __init__(self,url,browser_type):
        self.driver=self.open_browser(browser_type)
        self.driver.get(url)
    #调用浏览器
    def open_browser(self,browser_type):
        if browser_type=='chrome':
            driver = webdriver.Chrome()
            return driver
        elif browser_type=='firefox':
            driver = webdriver.Firefox()
            return driver
        else:
            print('type error')
    # 元素定位
    def locator(self,locator_type,value):
            if locator_type == 'xpath':
                el = self.driver.find_element_by_xpath(value)
                return el
            elif locator_type == 'id':
                el = self.driver.find_element_by_id(value)
                return el  
            elif locator_type == 'name':
                el = self.driver.find_element_by_name(value)
                return el
    # 输入
    def rew_input_text(self, locator_type, value, text):
            self.locator(locator_type, value).send_keys(text)
    # 点击
    def rew_click_element(self, locator_type, value):
            self.locator(locator_type, value).click()
if __name__ == '__main__':
    tk = TestKeyWords('http://www.jd.com','chrome')
    sleep(10)
    tk.rew_input_text('id', 'key', 'sss')
    sleep(2)
    tk.rew_click_element('xpath', '//*[@id="search"]/div/div[2]/button')