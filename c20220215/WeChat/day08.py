from pywinauto.application import Application
from c20220215.WeChat.settings import oaname
app1 = Application(backend='uia').start("E:\Program Files (x86)\Tencent\WeChat\WeChat.exe")  # 打开应用
app = Application(backend='uia').connect(process=16436)  # 连接应用 窗口id连接 每台电脑需从新更换 重启电脑需要重新校验
# 选择窗口
dlg = app.window(class_name='WeChatMainWndForPC')
dlg1 = app['微信']
leibiao1 = dlg1[u"ListBox4"]
# leibiao1.print_control_identifiers()
a=leibiao1.child_window(control_type="Text")
print(a)
