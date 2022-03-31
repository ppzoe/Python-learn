import time
from pywinauto.application import Application
from c20220215.WeChat.settings import oaname

app1 = Application(backend='uia').start("E:\Program Files (x86)\Tencent\WeChat\WeChat.exe")  # 打开应用 路径
# app = Application(backend='uia').connect(process=16436)  # 连接应用 窗口id连接 每台电脑需从新更换 重启电脑需要重新校验
app2 = Application(backend='uia').connect(path="E:\Program Files (x86)\Tencent\WeChat\WeChat.exe")  # 连接应用 路径
# 选择窗口 dlg 微信窗体
dlg = app2.window(class_name='WeChatMainWndForPC')
# 设置路径到会话列表 Sessions
Sessions = dlg[u"会话列表"]
# 设置路径到订阅列表 ListBox
ListBox = Sessions.children()[0].children()[2].children()[0].children()[0].children()[0].children()[1].children()[0]
# 设置路径到选中列表项目 SelectListItem
SelectListItem = ListBox.children()[1]
# 设置路径到 选中会话 SelectSession ps:也就是订阅号消息主页
SelectSession = SelectListItem.children()[0].children()[1].children()[2]
leibiao2 = SelectSession.children()[0].children()[0].children()[1]
leibiao2.click_input()
time.sleep(2)
# 订阅号正文 SubscriptionBody
dlg1 = app2.window(class_name='CefWebViewWnd')
SubscriptionBody = dlg1.children()[1].children()[0].children()[0]
# 关闭 正文 Close SubscriptionBody
Close = dlg1.children()[2].children()[0].children()[0].children()[3]
Close.click_input()
# leibiao3 = dlg.child_window().window(LocalizedControlType="ListItem")  # 选择到列表项目
# leibiao2.print_control_identifiers()
print(SubscriptionBody)
print(Close)
