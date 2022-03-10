import uiautomator2 as u2
from time import sleep
from c20220215.WeChat.settings import SJIP, oaname
import time
from urllib.parse import quote, unquote

d = u2.connect(SJIP)
d.app_start("com.tencent.mm", wait=True)  # 启动APP
list = oaname
d(resourceId="com.tencent.mm:id/he6").click()
for i in range(len(oaname)):
    print("序号：%s   值：%s" % (i + 1, list[i]))
    time.sleep(0.3)
    d.xpath(
        '//*[@resource-id="com.tencent.mm:id/fdi"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
    d.send_keys(list[i], clear=True)
    d.xpath(
        '//*[@resource-id="com.tencent.mm:id/hf1"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').click()
    time.sleep(0.3)
    d.xpath('//androidx.appcompat.widget.LinearLayoutCompat').click()
    d.swipe(0.8, 0.8, 0.8, 0.6)
    #
    time.sleep(1)
    # 该公众号最近的组信息
    recentnews = d.xpath('//*[@resource-id="com.tencent.mm:id/gy2"]/android.widget.LinearLayout[2]').info
    news = recentnews["childCount"]
    for a in range(1, news+1, 1):
        x_path = "//*[@resource-id='com.tencent.mm:id/gy2']/android.widget.LinearLayout[2]/android.view.ViewGroup[{}]".format(a)
        d.xpath(x_path).click()
        time.sleep(1)
        d.click(0.050, 0.065)
        time.sleep(0.3)
        print("+1")
    # d.xpath('//*[@resource-id="com.tencent.mm:id/gy2"]/android.widget.LinearLayout[2]/android.view.ViewGroup[1]').click()
    d.press("back")
    d.press("back")
    print("end")
time.sleep(0.3)
d.app_stop("com.tencent.mm")

# className = "android.view.ViewGroup"
# for i in X1:
#     d.xpath('//*[@resource-id="com.tencent.mm:id/gy2"]/android.widget.LinearLayout[2]/android.view.ViewGroup[' + i + ']').click()
#     d.press("back")

# 获取包名
# print(d.app_list_running())
# print(d.app_current())
