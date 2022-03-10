import unittest
from Test_selenium.Selenium_Python_WEB.f3_1 import TestKeyWords
from time import sleep


class TestForKey(unittest.TestCase):
    # 前置摄像头
    def setUp(self) -> None:
        print('setUp')

    # 后置摄像头
    def tearDown(self) -> None:
        print('tearDown')

    # 测试用例1
    def text_1(self):
        tk = TestKeyWords('https//www.jd.com', 'chrome')
        tk.input_text('id', 'kw', '神奇公司在哪里')
        tk.click_element('id', 'su')
        sleep(5)

    # 测试用例2
    def text_2(self):
        print('test_2')


if __name__ == '__main__':
    unittest.main()
