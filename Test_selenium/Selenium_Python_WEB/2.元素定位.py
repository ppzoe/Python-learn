import time

from selenium import webdriver
#创建浏览器对象
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Chrome()
# 跳转到指定URL
driver.get('http://www.baidu.com')
# 最大化窗口
driver.maximize_window()
'''
八种元素定位
1.id                    相当于身份证号码，一般情况下不会出现重复
2.name                  相当于身份证姓名，可能会出现重复
3.link text             主要基于超链接定位
4.partial link text     link text的模糊查询版本，类似于数据库中like %   当模糊查询到多个符合目标时提取第一个
                        当不要第一个时可用列表遍历  列表遍历，+s [] 如：dr=driver.find_elements_by_partial_link_text('百度')[1].text    print(dr)
5.classname             基于元素样式来进行定位，非常遇到重复的.一般不推荐使用，因为样式复杂下不易定位成功
6.tagname               标签名来进行定位，不推荐，一般重复的太多如div。只有在需要定位后进行二次筛选的情况下使用
7.css selector          应用相对较多的一种行为，最初IE浏览器不支持xpath，完全基于class属性来实现的定位
8.xpath                 目前应用最多的一种行为，基于页面结构来进行的定位
                            绝对路径：从html根路径下一层一层往下数，找到对应的层级，从而找到元素，除非十万火急，不要这么使用
                            相对路径：基于匹配制度来查找元素，依照xpath语法结构来走
                                例如：//*[@id'kw']
                                //表示从根路径下开始查找
                                *任意元素
                                []表示筛选条件（查找函数）
                                @表示基于属性来筛选，例如@id='kw'表示基于id属性值为kw的条件来进行筛选
                        确定xpath路径是否正确：
                            1.在开发者工具elements页面使用ctrl+f查找，进行判断
                            2.在console中输入$x()进行校验
                        如果要基于text来定位元素
                        在[]中添加text()="文本内容"进行查找，例如：//a[text()='新闻']
                        当元素无法直接定位时，可以通过子集元素返回父级来获取元素：~/..
                        //input[@id="kw"]
                        //input[contains(@id,'kw')]
                        contains表示进一步查找，匹配项模糊查找
                        //input[contains(text(),'百度')]
'''
#基于ID定位
# driver.find_element_by_id('id')
#基于name定位
# driver.find_element_by_name('name')
# 基于link text定位
# driver.get('http://baidu.com')
# driver.find_element_by_link_text('注册').click()
#基于partial link text 定位
# dr=driver.find_elements_by_partial_link_text('百度')
# for d in dr:
#     print(d.text)
#基于classname属性的定位
# driver.find_element_by_class_name('123')
#基于tagname的定位
# dr=driver.find_element_by_tag_name('a')
# for d in dr:
#         if d.text == '登录':
#             d.click()
# cssselector定位
# we_input=driver.find_element_by_css_selector('#kw')
# we_input.send_keys('无限')
# we_button=driver.find_element_by_css_selector('#su')
# we_button.click()
# xpath定位
driver.find_element(By.XPATH, "//a[text()='新闻']").click()
time.sleep(5)
driver.quit()
