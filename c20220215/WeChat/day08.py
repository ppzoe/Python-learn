import re
import time

import pyautogui
from pywinauto import mouse
from pywinauto.application import Application
from c20220215.WeChat.settings import oaname

# 获取屏幕分辨率，以便后面pyaotogui定位
pyautogui.size()
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
leibiao2.click_input()  # 点击
# 获取点击后鼠标的位置并存储
x, y = pyautogui.position()
# 等待2s
time.sleep(2)
# 订阅号正文 SubscriptionBody
dlg1 = app2.window(class_name='CefWebViewWnd')
SubscriptionBody = dlg1.children()[1].children()[0].children()[0]
# 关闭 正文 Close SubscriptionBody
Close = dlg1.children()[2].children()[0].children()[0].children()[3]
Close.click_input()
time.sleep(2)
# 列表向下10个滚轮
# pyautogui.scroll(-10)
mouse.scroll(coords=(x, y), wheel_dist=-3)
# leibiao3 = dlg.child_window().window(LocalizedControlType="ListItem")  # 选择到列表项目
# leibiao2.print_control_identifiers()
print(SubscriptionBody)
print(Close)
# def Zuye():
#     SelectListItem = ListBox.children()[1]
#     if len(SelectListItem.children()[0].children()[1].children()) == 3:
#         SelectSession = SelectListItem.children()[0].children()[1].children()[2]
#         return SelectSession
#     elif len(SelectListItem.children()[0].children()[1].children()) == 2:
#         SelectSession = SelectListItem.children()[0].children()[1].children()[1]
#         return SelectSession
#     else:
#         print("此用户没有消息")
#

# # 鼠标滚轮向下10次
#         scroll(coords=(0, 0), wheel_dist=10)

"吉林检察"
"通化检察"
"长春检察"
"长春林检"
"梨树检察"
"吉林市检察"
"延吉检声"
"敦化市检察院"
"延边林检"
"珲春林检"
"松原检察"
"吉林丰检"
"伊通检察"
"吉林省临江林区人民检察院"
"白山检察"
"辽源检察"
"南关检察"
"敦化林检"
"吉林省抚松林区人民检察院"
"九台检察"
"前郭检察"
"吉林昌邑检察"
"农安检察"
"梅河口市人民检察院"
"辽源西安检察"
"延边检察"
"宽城检察"
"洮南检察"
"扶余检察"
"长白检察"
"舒兰检察"
"和龙林检"
"白石山林检"
"辽源龙山检察"
"红石林检"
"白河林检"
"四平铁东检察"
"集安检察"
"珲春市人民检察院"
"长岭检察"
"船检"
"蛟河检察"
"双阳检察"
'四平检察'
"洮北检察"
"二道江检察院"
"江源林检"
"公主岭检察"
"龙井检察"
"永吉县人民检察院"
"桦甸检察"
"通化市东昌区人民检察院"
"和龙市人民检察院"
"东丰检察"
"通化县人民检察院"
"宁江检察"
"吉林高新检察"
"磐石检察"
"乾安检察"
"汪清林检"
"吉林市城西地区人民检察院"
"白城检察"
"图们检察"
"镇赉县人民检察院"
"双辽市人民检察院"
"汪清检察"
"净月检察"
"临江检察"
"浑江检察"
"德惠检察"
"城郊检察"
"柳河县人民检察院"
"通榆检察"
"西检在线"
"四平平东检察"
"大安检察"
"安图县人民检察院"
"绿园检察"
"抚检在线"
"江源区人民检察院"
"靖宇县人民检察院"
"正义辉检"
"长春市朝阳区人民检察院"
"榆树市人民检察院"
"长春经开检察院"
"长春高新检察"
"吉林省铁检分院"
"长春铁路运输检察院公众号"
"吉林铁检"
"白城铁检"
"通化铁路运输检察院"
"延边铁路运输检察院"
"正义龙潭"
"正义赉宁"
"二道检察"
"长春汽开检察"
"东辽检察"

