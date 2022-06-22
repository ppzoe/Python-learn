import time
import json
import requests
import pandas as pd

wbid = {"辽源西安检察": "5395116343",
        "吉林检察": "5093990523",
        "公主岭检察": "5584068981",
        "敦化检察": "5447470670",
        "图们市检察": "6353849316",
        "正义通化": "5879448076",
        "辽源龙山检察": "6385368516",
        "东丰检察": " 6378337633",
        "磐石检察": "6345559374",
        "长春检察": "5044195741",
        "吉林高新区人民检察院": "5970229924",
        "柳河检察": "6358803833",
        "敦化林区检察院": "5536828726",
        "吉林市龙潭检察": "5582921232",
        "白城检察": "5656903500",
        "白山检察": "6339831470",
        "吉林省铁检分院": "6339883980",
        "蛟河检察": "5574459823",
        "吉林市检察": "6343659076",
        "汪清检察": "5596927657",
        "辉南县检察院": "6356913596",
        "通榆检察": "6868416398",
        "长春宽检": "6306425503",
        "正义赉宁": "6611569218",
        "四平铁东检察": "5889528280",
        "集安检察": "5300072404",
        "延吉检声": "6254661126",
        "舒兰检察": "5584719581",
        "东昌检察": "6355286709",
        "延边林检": "5602838630",
        "抚松林检": "5591538937",
        "长春经开检察院": "6224300312",
        "乾安检察": "6410697440",
        "梅河口检察": "6358800766",
        "白石山林检": "5389080493",
        "安图检察": "6358225242",
        "东辽检察": "6385444059",
        "四平检察": "5613155684",
        "平东检察": "6366512642",
        "双阳检察": "6409812166",
        "长-岭-检-察": "6367720446",
        "南关检察服务在线": "5225824492",
        "红石林检": "5584234526",
        "前郭检察": "6351734919",
        "长春朝阳人民检察": "6362913846",
        "宁江检察": "6224459015",
        "正义通化县": "6313608038",
        "和龙市检察院": "5730455572",
        "镇赉检察": "6243330365",
        "二道检察": "6357757010",
        "白城铁路运输检察院": "6339944947",
        "龙井检察": "5041108193",
        "船营检察": "6348022249",
        "四平西检在线": "6410459024",
        "正义二道江": "6353210788",
        "靖宇县检察院": "5443607047",
        "浑江检察": "6336330372",
        "长春林检": "5586879074",
        "丰满检察": "6353058614",
        "吉林省临江林检": "5377551304",
        "长春城检": "6349379392",
        "长白检察": "6341709245",
        "松原检察": "5994742390",
        "桦甸检察": "6343822090",
        "双辽检察": "6478723023",
        "绿园检察": "5870154504",
        "汪清林检": "5688148923",
        "抚松检察": "2260040577",
        "珲春林检": "5608166483",
        "吉林省江源林检": "5539572886",
        "正义临江": "6339948850",
        "和龙林检": "5687050104",
        "长春铁路运输检察院": "6188894104",
        "净月检察": "6346900298",
        "农安检察": "6353824387",
        "吉林市城西地区人民检察院": "6190083636",
        "吉林省榆树市检察院": "5680421614",
        "正义珲春": "5586347338",
        "延边检察": "6336750039",
        "长春汽开检察": "6407255114",
        "延边铁检": "6373350257",
        "永吉检察": "6345561231",
        "江源检察": "6339840034",
        "吉林伊通检察": "6195789197",
        "长春新区检务在线": "6359316906",
        "吉林铁路运输检察院": "6352188265",
        "大安检察": "6351109634",
        "德惠检察": "6369869837",
        "正义梨树": "6373328219",
        "白河林检": "5607093006",
        "洮南检察在线": "6349941756",
        "洮北检察": "5852251873",
        "九台检察": "6385741999",
        "辽源检察": "6348340193",
        "吉林昌邑检察": "5577643587",
        "通化铁路运输检察院1": "6431327013",
        "扶余检察": "6385694129",
        }

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    "cookie": "SINAGLOBAL=9647412095234.6.1640246418846; UOR=www.baidu.com,weibo.com,www.baidu.com; wvr=6; webim_unReadCount=%7B%22time%22%3A1654503479042%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A36%2C%22msgbox%22%3A0%7D; SCF=AguY-Aj-Uaa6bVkTQCb9K5idnPXvJY2CmhVzApDg1Yb3bqPenUgPdjdFDKEENhnlRwEFRcw-29iabJj15Cohceo.; XSRF-TOKEN=uUCc67CfWuFt4Zx8Hc6QmH8C; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; _s_tentry=weibo.com; Apache=7677633712632.539.1654567754121; ULV=1654567754133:10:3:3:7677633712632.539.1654567754121:1654504463848; PC_TOKEN=41d18ef36e; login_sid_t=64f4ab280918ce7754655d58f09b860f; cross_origin_proto=SSL; wb_view_log=1920*10801; SUB=_2A25PmoLJDeRhGeRK61MU9CfJzzmIHXVs0fMBrDV8PUNbmtB-LVTDkW9NU3tst4j0z1eFrYV4ZlwFAESFPlTQUvE5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF01YMUE2SQUse1CbGJT33q5JpX5KzhUgL.FozXeh2fSh.fSh-2dJLoI0qLxK-LBo.LBoeLxKqLBoMLBK2LxKBLBonLBoqLxK-L12qL1hnLxK-LBKqL1hzLxKBLB.BL1K-t; ALF=1686119961; SSOLoginState=1654583961; WBPSESS=Dt2hbAUaXfkVprjyrAZT_KMMtYfqHFQ97PhyvVJf9XrZ2k9Or2uPRQOS_crKzb2rT1HAwg0msZUzYtP0jWVyfmKoLqdze4EC1bsW07I4dKtBbF0fzN-pNbbyJXHuP8PKlMCOilpc0-L32x1IQDCYRxZqGfKMvKgKV18BTr9xuppgcUXW51nA74tMKBBZhRW0zIbSbdvz_mwAg2c95VTfIA=="

}

# uid, 目标对象id
uid = "5093990523"
# 页数
page = "1"
# stat,stat_date搜索范围年，月. 如：202205 2022年5月的数据
stat = "202205"
url = "https://weibo.com/ajax/profile/info?custom=" + uid

urls = "https://weibo.com/ajax/statuses/mymblog?uid=" + uid + "&page=" + page + "&feature=0&stat_date=" + stat
wb = requests.get(url, headers=headers)
wb.encoding = "utf-8"
# wbhome 微博主页信息
wbhome = requests.get(url, headers=headers)
wbhome.encoding = "utf-8"
wbhome_dic = wbhome.json()  # json转字典
# screen_name 微博名称
screen_name = wbhome_dic["data"]["user"]["screen_name"]
# followers_count 粉丝数
followers_count = wbhome_dic["data"]["user"]["followers_count"]
# followers_count_str 粉丝数简写
followers_count_str = wbhome_dic["data"]["user"]["followers_count_str"]
# uid 微博号识别标识
uid = wbhome_dic["data"]["user"]["id"]
# verified_reason 验证原因
verified_reason = wbhome_dic["data"]["user"]["verified_reason"]
# location 位置，所在地
location = wbhome_dic["data"]["user"]["location"]

print(wbhome.json())
print("微博名称： " + str(screen_name))
print("粉丝数： " + str(followers_count))
print("粉丝数简写： " + str(followers_count))
print("微博号识别标识： " + str(uid))
print("验证原因： " + str(verified_reason))
print("位置，所在地： " + str(location))

"""
旧版微博：https://weibo.com/2401549545/profile?rightmod=1&wvr=6&mod=personinfo&is_all=1
https://weibo.com/u/2835724503?refer_flag=0000015010_&from=feed&loc=avatar
新版微博：https://weibo.com/u/2401549545

https://weibo.com/ajax/statuses/mymblog?uid=5093990523&page=1&feature=0

https://weibo.com/ajax/statuses/mymblog?uid=5093990523&page=1&feature=0&stat_date=202205

cookie:[
SINAGLOBAL=9647412095234.6.1640246418846; 
SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF01YMUE2SQUse1CbGJT33q5JpX5KMhUgL.FozXeh2fSh.fSh-2dJLoI0qLxK-LBo.LBoeLxKqLBoMLBK2LxKBLBonLBoqLxK-L12qL1hnLxK-LBKqL1hzLxKBLB.BL1K-t;
UOR=www.baidu.com,weibo.com,www.baidu.com; 
wvr=6; 
webim_unReadCount={"time":1654503479042,"dm_pub_total":1,"chat_group_client":0,"chat_group_notice":0,"allcountNum":36,"msgbox":0}; ALF=1686103471; SSOLoginState=1654567472; 
SCF=AguY-Aj-Uaa6bVkTQCb9K5idnPXvJY2CmhVzApDg1Yb3bqPenUgPdjdFDKEENhnlRwEFRcw-29iabJj15Cohceo.; 
SUB=_2A25PmsJgDeRhGeRK61MU9CfJzzmIHXVs0bSorDV8PUNbmtB-LRmlkW9NU3tst2IqNAeWVsaUnl2wJ-vwch_aKc8f; 
XSRF-TOKEN=uUCc67CfWuFt4Zx8Hc6QmH8C; 
SL_G_WPT_TO=zh; 
SL_GWPT_Show_Hide_tmp=1; 
SL_wptGlobTipTmp=1; _s_tentry=weibo.com; 
Apache=7677633712632.539.1654567754121; 
ULV=1654567754133:10:3:3:7677633712632.539.1654567754121:1654504463848; 
WBPSESS=fLtleuy1hZ_tMMSUlLky_guMBFx5g9XNCfQekiz42ZytU-PpQSiutZ1J6yxdxoR15af62BCJ_zTIIhhHc1i-7ZKaPixuIJ8snbyEXqxUQECgEowv6x4hD2cVcCN-liyKBBZXTyudF-khbdXqWnH5rg==
]
reads_count 阅读数
reposts_count 转发数
repost_type: 3 此条微博的类型为转发 
repost_type: 1 此条微博的类型为快转
retweeted_status 转发原微博的数据列表
created_at 发布时间
comments_count 评论数 
attitudes_count 点赞数
id  文章id
"""
wb.close()
