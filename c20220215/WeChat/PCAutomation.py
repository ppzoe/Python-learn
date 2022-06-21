import time

from pywinauto.application import Application
import pyautogui
import win32api
import win32con
from pywinauto import mouse
from c20220215.WeChat.settings import oaname, oaX


def zhuye(SelectListItem, app2):  # zhuye()函数，判断并循环点击每一组的文章，判断文章样式选择不同路径
    if len(SelectListItem.children()[0].children()[1].children()) == 3:
        SelectSession = SelectListItem.children()[0].children()[1].children()[2]
        # 设置路径到 选中会话 SelectSession ps:自定义函数，内容组样式不同一导致路径不同一，可用此函数判断，也就是订阅号消息主页
        if len(SelectSession.children()) == 3:  # 判断文章组是否首篇文章放大，放大执行此分支
            # leibiao 一组文章中的第一个
            leibiao = SelectSession.children()[0].children()[0].children()[1]
            leibiao.click_input()  # 点击
            # 获取点击后鼠标的位置并存储
            x, y = pyautogui.position()
            # 等待 正文加载
            time.sleep(5)

            # 订阅号正文 SubscriptionBody
            dlg1 = app2.window(class_name='CefWebViewWnd')
            # SubscriptionBody = dlg1.children()[1].children()[0].children()[0]

            # 关闭 正文 Close SubscriptionBody
            dlg1.close()
            # 列表向下移动12个滚轮的距离
            # mouse.scroll(coords=(x, y), wheel_dist=-4)
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -530)

            # leibiao1 一组文章中除去首个文章的列表
            leibiao1 = SelectSession.children()[2].children_texts()  # children_texts()获取控件子项的文本
            nlists = len(leibiao1)  # 一组文章中除去首个文章,其余文章的数量
            print("剩余文章" + str(nlists))

            for i in range(len(leibiao1)):  # 遍历此组剩下的文章
                time.sleep(1)
                leibiao2 = SelectSession.children()[2].children()[i].children()[0].children()[1]
                leibiao2.click_input()  # 点击
                # 等待 正文加载
                time.sleep(5)
                # 关闭 正文 Close SubscriptionBody
                print(type(dlg1))
                dlg1.close()
                # 鼠标位置回到记录点
                mouse.scroll(coords=(x, y))
                # 鼠标向下滚动一定距离
                win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -290)
        elif len(SelectSession.children()) == 2:  # 判断文章组没有首篇放大文章组时，执行此分支
            # 获取点击后鼠标的位置并存储
            x, y = pyautogui.position()
            # leibiao 此组文章列表，子项
            leibiao = SelectSession.children()[1].children_texts()  # children_texts()获取控件子项的文本
            xlists = len(leibiao)  # 本组文章总数
            print("剩余文章" + str(xlists))
            for i in range(len(leibiao)):  # 遍历此组剩下的文章
                time.sleep(1)
                leibiao2 = SelectSession.children()[1].children()[i].children()[0].children()[1]
                leibiao2.click_input()  # 点击
                # 等待 正文加载
                time.sleep(5)
                dlg1 = app2.window(class_name='CefWebViewWnd')
                # 关闭 正文 Close SubscriptionBody
                print(type(dlg1))
                dlg1.close()
                # 鼠标位置回到记录点
                mouse.scroll(coords=(x, y))
                # 鼠标控制列表向下滚动一定距离
                win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -320)

    elif len(SelectListItem.children()[0].children()[1].children()) == 2:
        SelectSession = SelectListItem.children()[0].children()[1].children()[1]
        leibiao = SelectSession.children()[0].children()[1]
        leibiao.click_input()  # 点击

        # 获取点击后鼠标的位置并存储
        x, y = pyautogui.position()
        # 等待 正文加载
        time.sleep(5)

        # 订阅号正文 SubscriptionBody
        dlg1 = app2.window(class_name='CefWebViewWnd')
        # SubscriptionBody = dlg1.children()[1].children()[0].children()[0]

        # 关闭 正文 Close SubscriptionBody
        dlg1.close()
        # 鼠标位置回到记录点
        mouse.scroll(coords=(x, y))
        # 鼠标向下滚动一定距离
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -550)
        time.sleep(1)

    else:
        print("此用户没有消息")


def min():
    # 获取屏幕分辨率，以便后面pyaotogui定位
    pyautogui.size()
    # 打开应用 路径
    app1 = Application(backend='uia').start("E:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
    # 连接应用 窗口id连接 每台电脑需从新更换 重启电脑需要重新校验
    # app = Application(backend='uia').connect(process=16436)
    # 连接应用 路径
    app2 = Application(backend='uia').connect(path="E:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
    # 选择窗口 dlg 微信窗体
    dlg = app2.window(class_name='WeChatMainWndForPC')
    # 循环主体 settings文件中设置 oaname ，循环完设置中的oaname为止
    for i in range(len(oaname)):
        # 选中搜索控件
        souso = dlg.child_window(title="搜索", control_type="Edit")
        souso.click_input()
        time.sleep(0.5)
        # 搜索控件内输入公众号名称
        souso.type_keys('^a').type_keys(oaname[i], with_spaces=True)
        time.sleep(1)
        souso.type_keys('{ENTER}')

        # 设置路径到会话列表 Sessions
        Sessions = dlg[u"会话列表"]

        # 设置路径到公众号文章列表 ListBox
        ListBox = \
            Sessions.children()[0].children()[2].children()[0].children()[0].children()[0].children()[1].children()[0]

        for a in range(oaX):  # oaX可在settings中设置，控制每个公众号循环查询的组数
            try:  # 组数低于oaX时会报错，indexerror 则跳出循环
                # 设置路径到公众号文章列表中发布内容组的列表 SelectListItem
                print("第" + str(a + 1) + "组")
                SelectListItem = ListBox.children()[a + 1]
                zhuye(SelectListItem, app2)
            except IndexError:
                break
            except Exception as e:
                print(e)


if __name__ == '__main__':
    min()
