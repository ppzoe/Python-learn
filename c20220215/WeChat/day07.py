from pywinauto.application import Application
from c20220215.WeChat.settings import oaname
app1 = Application(backend='uia').start("E:\Program Files (x86)\Tencent\WeChat\WeChat.exe")  # 打开应用
app = Application(backend='uia').connect(process=13696)  # 连接应用 窗口id连接 每台电脑需从新更换
# 选择窗口
dlg = app.window(class_name='WeChatMainWndForPC')
dlg1 = app['微信']
# 选中控件
souso = dlg1.child_window(title="搜索", control_type="Edit")
# 点击控件
souso.click_input()
# 控件内输入数据
# for i in range(len(oaname)):
#     souso.type_keys('^a').type_keys(oaname[i], with_spaces=True).type_keys('{ENTER}')

# 点击按钮
leibiao = dlg1["ListBox"]  # (control_type="ListItem")
leibiao1 = app['微信'][u"ListBox4"]
# leibiao2 = leibiao1.children(best_match="ListItem")
leibiao3 = leibiao1.child_window(best_match="ListItem2").window_text()


# Button = leibiao1.child_window(title="人民日报", control_type="Button")
# Button.click_input()
# leibiao11 = leibiao.child_window(title="人民日报", control_type="ListItem")
# leibiao2 = leibiao1['人民日报ListItem']

# print(leibiao2)
print(leibiao3)


# edit = souso.child_window(title="搜索", control_type="Edit")
# edit.print_control_identifiers()

# pic = dlg1.capture_as_image()  # 截图
# print(pic)
# pic.save('01.png')

