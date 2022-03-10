import re
import time
import requests
from lxml import etree

# 首先注册微信公众号，比较简单快速

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 S'
                  'afari/537.36 QBCore/4.0.1278.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWe'
                  'bKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5'
                  ' WindowsWechat',
    # 微信公众平台的cookies
    'Cookie': "RK=IWT9GknfGE; ptcz=f791cdcac8395c84d535f2cabcdaead23b4ab8fa632c2add054e4aafa48699b4; o_cookie=384110237;"
              " pac_uid=1_384110237; tvfe_boss_uuid=7c36d631cac97e11; pgv_pvid=315006831; iip=0; ua_id=d4KuO9dRVpRszySRA"
              "AAAAAbUrDGumHyNLguQG7UG_l8=; wxuin=40656984961963; mm_lang=zh_CN; ts_uid=5215990812; ptui_loginuin=384110"
              "237; xid=2a0fd086299abaccd4ef2a98d369d2dd; rewardsn=; wxtokenkey=777; SL_GWPT_Show_Hide_tmp=1; SL_wptGlob"
              "TipTmp=1",

}

simple_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116'
                  ' Safari/537.36 QBCore/4.0.1278.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI '
                  'MicroMessenger/7.0.5 WindowsWechat',

}


def search_biz(query):
    # 根据公众号名称 搜索公众号
    url = 'https://mp.weixin.qq.com'
    req = requests.get(url, headers=header)
    token = re.findall(r'token=(\d+)', str(req.url))[0]
    # print(token)
    url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
    data = {
        'action': 'search_biz',
        'begin': '0',
        'count': '5',
        'query': query,
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1'
    }
    res = requests.get(url, headers=header, params=data)
    return res.json().get('list')[0].get('fakeid')


def get_pages(fakeid, token, all=False):
    # 获取 翻页
    url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
    page = 0
    max_num = 5
    result = []
    while page * 5 < max_num:
        params = {
            'action': 'list_ex',
            'begin': str(page * 5),
            'count': '5',
            'fakeid': fakeid,
            'type': '9',
            'query': '',
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1'
        }
        res = requests.get(url, params=params, headers=header)
        if all:
            max_num = res.json().get('app_msg_cnt')
        msg_lists = res.json().get('app_msg_list')
        for msg_list in msg_lists:
            # cover 封面 link 链接 digest '描述' title '标题'
            # aid = msg_list.get('aid')
            link = msg_list.get('link')
            # digest = msg_list.get('digest') #
            title = msg_list.get('title')
            create_time = time.localtime(int(msg_list.get('create_time')))
            otherStyleTime = time.strftime("%Y-%m-%d", create_time)
            result.append((link, title, otherStyleTime))
        page += 1
    return result
