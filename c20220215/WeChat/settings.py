# SJIP = "192.168.0.110:5555"
SJIP = "127.0.0.1:62001"
# oaname = ['净月检察', '长春检察']
oaname = ['梨树检察', '人民日报']
# oaX 微信公众号oaX组信息
oaX = 7
'''
adb connect 192.168.0.110:5555  # 连接移动设备 ip 192.168.0.110 端口 5555 
# ps：雷电模拟器端口：5555 夜神模拟器端口：62001 逍遥安卓模拟器端口：21503 海马玩模拟器端口：53001 网易MUMU模拟器端口：7555
#初始化安装
adb connect ip地址:5555
python -m uiautomator2 init
#启动 
python -m weditor
# git clone https://github.com/alibaba/web-editor 部署包
adb devices  # 查看连接设备

mitmdump -s weixinDatacaught.py   # 启动 mitm监听 
需要代理被监控对象 127.0.0.1:8080



adb connect 192.168.0.105:62001
python -m uiautomator2 init
python -m weditor
'''
