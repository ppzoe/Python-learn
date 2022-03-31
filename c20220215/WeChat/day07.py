from pywinauto.application import Application
from c20220215.WeChat.settings import oaname
app1 = Application(backend='uia').start("E:\Program Files (x86)\Tencent\WeChat\WeChat.exe")  # 打开应用
app = Application(backend='uia').connect(path="E:\Program Files (x86)\Tencent\WeChat\WeChat.exe")   # 连接应用 窗口id连接 每台电脑需从新更换
# 选择窗口
dlg = app.window(class_name='WeChatMainWndForPC')  # 微信窗口
dlg1 = app.window(class_name='CefWebViewWnd')      # 公众号正文窗体
# 选中控件
souso = dlg.child_window(title="搜索", control_type="Edit")
# 点击控件
souso.click_input()
# 控件内输入数据
for i in range(len(oaname)):
    souso.type_keys('^a').type_keys(oaname[i], with_spaces=True)

    souso.type_keys('{ENTER}')

    # 点击按钮
    # 设置路径到会话列表 Sessions
    Sessions = dlg[u"会话列表"]
    # 设置路径到订阅列表 ListBox
    ListBox = Sessions.children()[0].children()[2].children()[0].children()[0].children()[0].children()[1].children()[0]
    # 设置路径到选中列表项目 SelectListItem
    SelectListItem = ListBox.children()[1]
    # 设置路径到 选中会话 SelectSession ps:也就是订阅号消息主页
    SelectSession = SelectListItem.children()[0].children()[1].children()[2]
    # leibiao2 = SelectSession.children()[0].children()[1]
    # leibiao2.click_input()
    # # 订阅号正文 SubscriptionBody
    # SubscriptionBody = dlg1.children()[1].children()[0].children()[0]
    # # 关闭 正文 Close SubscriptionBody
    # Close = dlg1.children()[2].children()[0].children()[0].children()[3]
    # Close.click_input()
    print(SelectSession)


# Button = leibiao1.child_window(title="人民日报", control_type="Button")
# Button.click_input()
# leibiao11 = leibiao.child_window(title="人民日报", control_type="ListItem")
# leibiao2 = leibiao1['人民日报ListItem']



# edit = souso.child_window(title="搜索", control_type="Edit")
# edit.print_control_identifiers()

# pic = dlg1.capture_as_image()  # 截图
# print(pic)
# pic.save('01.png')

