# SJIP = "192.168.0.110:5555"
SJIP = "127.0.0.1:62001"
# oaname = ['净月检察', '长春检察']
oaname = ["吉林检察",
          "通化检察",
          "长春检察",
          "长春林检",
          "梨树检察",
          "吉林市检察",
          "延吉检声",
          "敦化市检察院",
          "延边林检",
          "珲春林检",
          "松原检察",
          "吉林丰检",
          "伊通检察",
          "吉林省临江林区人民检察院",
          "白山检察",
          "辽源检察",
          "南关检察",
          "敦化林检",
          "吉林省抚松林区人民检察院",
          "九台检察",
          "前郭检察",
          "吉林昌邑检察",
          "农安检察",
          "梅河口市人民检察院",
          "辽源西安检察",
          "延边检察",
          "宽城检察",
          "洮南检察",
          "扶余检察",
          "长白检察",
          "舒兰检察",
          "和龙林检",
          "白石山林检",
          "辽源龙山检察",
          "红石林检",
          "白河林检",
          "四平铁东检察",
          "集安检察",
          "珲春市人民检察院",
          "长岭检察",
          "船检",
          "蛟河检察",
          "双阳检察",
          '四平检察',
          "洮北检察",
          "二道江检察院",
          "江源林检",
          "公主岭检察",
          "龙井检察",
          "永吉县人民检察院",
          "桦甸检察",
          "通化市东昌区人民检察院",
          "和龙市人民检察院",
          "东丰检察",
          "通化县人民检察院",
          "宁江检察",
          "吉林高新检察",
          "磐石检察",
          "乾安检察",
          "汪清林检",
          "吉林市城西地区人民检察院",
          "白城检察",
          "图们检察",
          "镇赉县人民检察院",
          "双辽市人民检察院",
          "汪清检察",
          "净月检察",
          "临江检察",
          "浑江检察",
          "德惠检察",
          "城郊检察",
          "柳河县人民检察院",
          "通榆检察",
          "西检在线",
          "四平平东检察",
          "大安检察",
          "安图县人民检察院",
          "绿园检察",
          "抚检在线",
          "江源检察",
          "靖宇县人民检察院",
          "正义辉检",
          "长春市朝阳区人民检察院",
          "榆树市人民检察院",
          "长春经开检察院",
          "长春新区检察院",
          "吉林省铁检分院",
          "长春铁路运输检察院公众号",
          "吉林铁检",
          "白城铁检",
          "通化铁路运输检察院",
          "延边铁路运输检察院",
          "正义龙潭",
          "正义赉宁",
          "二道检察",
          "长春汽开检察",
          "东辽检察"]
# oaX 微信每个公众号向下遍历oaX组信息
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
