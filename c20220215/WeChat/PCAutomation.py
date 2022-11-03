import time
import re   
import datetime
from pywinauto.application import Application
import pyautogui
import win32api
import win32con
from pywinauto import mouse
from c20220215.WeChat.settings import oaname, oaX


def release_time(SelectListItem,theTime):  # 公众号发布时间
    time.sleep(2)
    # release_time1 = dlg.children()[1].children()[0].children()[0]
    release_time1 = SelectListItem.children()[0].children()[1].children()[0].children()[1]
    r_time = str(release_time1)
    # r_1 = re.search(r"(\d{4}-\d{1,2})", r_time).group(0)
    r_1 = re.search(r'\'(.*?)\'', r_time).group(0) if re.search(r'\'(.*?)\'', r_time) is not None else ''
    r_list1 = ["星期", "昨天", "期一", "期二", "期三", "期四", "期五", "期六", "期日"]
    r_list = [" 0", " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9"]
    if r_list1.count(r_1[1:3]) > 0:
        print(r_1)
        print(r_1[1:3])
        r_2 = theTime
        return r_2
    elif r_list.count(r_1[1:3]) > 0:
        print(r_1[1:4])
        r_2 = theTime
        return r_2
    else:
        pub_Time = r_1[1:-1]
        r_3 = time.strptime(pub_Time, u"%Y年%m月%d日  %H:%M")
        print(r_3)
        return r_3


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
            # 判断日期，与设置年月时间相同则会停止对此公众号的遍历
            if mi_time > release_time(SelectListItem, theTime):
                dlg1.close()
                print(release_time(SelectListItem, theTime))
                print(mi_time)
                deadline.append("截止日期已到达1")
                return

            else:
                # 关闭 正文 Close SubscriptionBody
                dlg1.close()
                # 列表向下移动12个滚轮的距离
                # mouse.scroll(coords=(x, y), wheel_dist=-4)
                win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -480)
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
                    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -280)
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
                win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -290)

    elif len(SelectListItem.children()[0].children()[1].children()) == 2:
        SelectSession = SelectListItem.children()[0].children()[1].children()[1]
        leibiao = SelectSession.children()[0].children()[1]
        leibiao.click_input()  # 点击

        # 获取点击后鼠标的位置并存储
        x, y = pyautogui.position()
        # 等待 正文加载
        time.sleep(4)

        # 订阅号正文 SubscriptionBody
        dlg1 = app2.window(class_name='CefWebViewWnd')
        # SubscriptionBody = dlg1.children()[1].children()[0].children()[0]
        # 判断日期，与设置年月时间相同则会停止对此公众号的遍历
        if mi_time > release_time(SelectListItem, theTime):
            dlg1.close()
            print(release_time(SelectListItem, theTime))
            print(mi_time)
            deadline.append("截止日期已到达1")
            return
        else:
            # 关闭 正文 Close SubscriptionBody
            dlg1.close()
            # 鼠标位置回到记录点
            mouse.scroll(coords=(x, y))
            # 鼠标向下滚动一定距离
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -500)
            time.sleep(0.5)

    else:
        print("此用户没有消息")


def select_list(Sessions):  # 判断是否需要切换到列表模式
    model = Sessions.children()[0].children()[0].children()[0].children()[0]
    if model.texts() == ['订阅号']:    # 如果此路径下texts名称为['订阅号']模式为卡片模式 ，需要点击列表模式按键
        print("进入传统列表模式")
        Card = Sessions.children()[0].children()[0].children()[0].children()[1].children()[0]  # 切换至列表模式按键路径
        Card.click_input()  # 点击 切换到列表模式
        time.sleep(0.5)


def subscription(dlg):  # 进入订阅号列表页面
    a = "订阅号"
    # 选中搜索控件
    souso = dlg.child_window(title="搜索", control_type="Edit")
    souso.click_input()
    time.sleep(0.5)
    # 搜索控件内输入“订阅号”
    souso.type_keys('^a').type_keys(a, with_spaces=True)
    time.sleep(0.5)
    souso.type_keys('{ENTER}')
    subscribe = dlg["搜索结果"].children()[1].children()[0]
    subscribe.click_input()


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
    # 设置路径到会话列表 Sessions
    Sessions = dlg[u"会话列表"]
    # 进入订阅号列表页面
    subscription(dlg)
    # 调用函数判断是否为列表模式，如不是择自动点击到列表模式
    select_list(Sessions)
    # 循环主体 settings文件中设置 oaname ，循环完设置中的oaname为止
    for i in range(len(oaname)):
        deadline.clear()  # 初始化截止日期判断列表
        # 选中搜索控件
        souso = dlg.child_window(title="搜索", control_type="Edit")
        souso.click_input()
        time.sleep(0.5)
        # 搜索控件内输入公众号名称
        souso.type_keys('^a').type_keys(oaname[i], with_spaces=True)
        time.sleep(1)
        souso.type_keys('{ENTER}')

        # 设置路径到公众号文章列表 ListBox
        ListBox = \
            Sessions.children()[0].children()[0].children()[2].children()[0].children()[0].children()[0].children()[1].children()[0]
        for a in range(oaX):  # oaX可在settings中设置，控制每个公众号循环查询的组数
            try:  # 组数低于oaX时会报错，indexerror 则跳出循环
                # 设置路径到公众号文章列表中发布内容组的列表 SelectListItem
                print("第" + str(a + 1) + "组")
                SelectListItem = ListBox.children()[a + 1]
                zhuye(SelectListItem, app2)
                print(deadline)
                if not deadline:  # 如果列表为空继续循环
                    continue
                else:           # 如果列表不为空跳出本层循环
                    break
            except IndexError:
                break
            except Exception as e:
                print(e)


if __name__ == '__main__':
    deadline = []
    print("请输入查询最小日期 如2022年5月 输入'2022-05'")
    mi_time1 = input("")
    mi_time = time.strptime(mi_time1, '%Y-%m')
    ISOTIMEFORMAT = '%Y-%m'
    the_Time = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    theTime = time.strptime(the_Time, '%Y-%m')
    min()
