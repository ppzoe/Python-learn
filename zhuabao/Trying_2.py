
""" 网络数据包捕获与分析程序 """

import pcap
import dpkt
import json
import re
import time
import urllib.request

# 过滤输出目标ip
dst_lists = [
    '203.66.1.212',  # nslookup dpdcs.4399sy.com.hk
    '52.74.10.186',  # nslookup dpdcs.4399en.com
    '52.58.69.212',  # nslookup dpdcs.4399sy.ru
    '220.241.11.3',  # nslookup dpdcs.4399th.com
    '124.243.195.63',  # nslookup sdkdcs.4399sy.com
    '42.62.106.216',  # nslookup udpdcs.4399sy.com
    '42.62.106.230',  # nslookup udpdcs.4399sy.com
]

req_data = ""
times = 0


def capt_data(eth_name="eth0", p_type=None):
    """
    捕获网卡数据包
    :param eth_name  网卡名，eg. eth0,eth3...
    :param p_type    日志捕获类型 1：sdk日志用例分析 2：目标域名过滤输出 3：原始数据包
    :return:
    """

    pc = pcap.pcap(eth_name)
    pc.setfilter('tcp port 80')  # 设置监听过滤器
    print ('start capture....')
    if pc:
        for p_time, p_data in pc:  # p_time为收到时间，p_data为收到数据
            anly_capt(p_time, p_data, p_type)


def anly_capt(p_time, p_data, p_type):
    """
    解析数据包
    :param p_data  收到数据
    :param p_type  日志捕获类型 1：sdk日志用例分析 2：目标域名过滤输出 3：原始数据包
    :return:
    """

    p = dpkt.ethernet.Ethernet(p_data)
    if p.data.__class__.__name__ == 'IP':
        ip_data = p.data
        src_ip = '%d.%d.%d.%d' % tuple(map(ord, list(ip_data.src)))
        dst_ip = '%d.%d.%d.%d' % tuple(map(ord, list(ip_data.dst)))
        if p.data.data.__class__.__name__ == 'TCP':
            tcp_data = p.data.data
            if tcp_data.dport == 80:
                # print tcp_data.data
                if tcp_data.data:
                    # 调用日志模块，对日志进行处理
                    if p_type == 1:
                        # sdk日志用例分析
                        if dst_ip in dst_lists:
                            tmp = tcp_data.data.strip()
                            global req_data, times
                            if tmp.startswith("POST") or tmp.startswith("GET"):  # or times > 0
                                if req_data:
                                    haiwai_log_case(req_data)
                                req_data = tmp + "\n"
                                # times = 0
                            else:
                                req_data = req_data + tmp
                                # times = times + 1

                    elif p_type == 2:
                        # 目标域名过滤输出
                        if dst_ip in dst_lists:
                            print ("tcp_data:", tcp_data.data)

                    else:
                        # 无过滤条件输出
                        print ("tcp_data:", tcp_data.data)


# android 日誌類型，从data中获取
log_type_from_data = {

    'open_game': u'[打开游戏]',
    'network_check': u'[网络监测]',
    'open_login': u'[登录界面前]',
    'select_server': u'[选服日志]',
    'create_role': u'[创角日志]',
    'role_level_change': u'[等级日志]',

    # 海外,俄语
    'activity_open': u'[打开游戏]',
    'load_start_before_login': u'[加载开始]',
    'load_finish_before_login': u'[加载结束]',
    'activity_before_login': u'[登录界面前]',
    'click_enter': u'[进入游戏]',
    'get_user_server_login': u'[选服日志]',
    'user_create_role': u'[创角日志]',
    'role_login': u'[角色登录]',
    'enter_success': u'[成功进入游戏]',
    'role_level': u'[等级日志]',
    'user_online': u'[在线日志]',
    'exit_success': u'[退出游戏]',

}

# ios日誌類型，从请求资源路径获取
log_type_from_path = {
    'activity_open.php': u'[打开游戏]',
    'load_start_before_login.php': u'[加载开始]',
    'load_finish_before_login.php': u'[加载结束]',
    'activity_before_login.php': u'[登录界面前]',
    'click_enter.php': u'[进入游戏]',
    'get_user_server_login.php': u'[选服日志]',
    'user_create_role.php': u'[创角日志]',
    'role_login.php': u'[角色登录]',
    'enter_success.php': u'[成功进入游戏]',
    'user_online.php': u'[在线日志]',
    'role_level.php': u'[等级日志]',
    'exit_success.php': u'[退出游戏]',
    'share.php': u'[分享日志]',
    'init_info.php': u'[初始化日志]',
    'event.php': u'[事件日志]',
    'user_login.php': u'[user_login]',
    'user_server_login.php': u'[user_server_login]',
    'enter_game.php': u'[enter_game]',
}

# 过滤path
filter_out_list = [
    'u/',
    'plugin/error/check',
    'service/version/get_info',
]

# 过滤打印出属于列表中的host的日志。
host_list = [
    'dpdcs.4399sy.com.hk',
    'dpdcs.4399en.com',
    'dpdcs.4399sy.ru',
    'dpdcs.4399th.com',
    'sdkdcs.4399sy.com',
    'udpdcs.4399sy.com',
]


def formattime(t):  # 日期字段格式化
    return time.strftime('%c', time.gmtime(t + 8 * 3600))


def req_to_dict(req_string):
    """
    将请求数据转换为dic
    :param req_string:
    :return:
    """
    req_dict = {}
    req_string = req_string.strip()
    if len(req_string) > 0:
        req_string = urllib.request.unquote(req_string)
        # print "req_string_after_unquote:",req_string
        m1 = re.search("(GET|POST)(.*)\?(.*)HTTP/1.1", req_string)  # (method,path,param)
        m2 = re.search("Host:(.*)", req_string)  # (host,)
        # m3 = re.search("\sdata=(.*)\s", req_string)  # (body,)
        m4 = re.search("\sdata=([\s\S]*)", req_string)  # (body,)
        # m5 = re.search("eventTime\":\"(\d+)", req_string)  # (eventTime,)
        m5 = re.search("eventTime\"\s*:\s*\"(\d+)", req_string)
        if m1:
            req_dict["method"] = m1.group(1).strip()
            req_dict["path"] = m1.group(2).strip()[1:]
            param_string = m1.group(3).strip()
            if param_string:
                param_string = param_string.split("&")
                param_dict = {}
                for item in param_string:
                    tmp_list = item.split("=")
                    if len(tmp_list) > 1:
                        param_dict[tmp_list[0]] = tmp_list[1]
                req_dict["param"] = param_dict
        if m2:
            req_dict["host"] = m2.group(1).strip()
        if m4:
            try:
                body = m4.group(1).replace("\n", "")
                body = json.loads(body)
            except ValueError:
                print ("\033[1;31;40m")
                print ("m4:Error:body ValueError,req_string-->%s" % req_string)
                print ("\033[0m")
                body = {}
            req_dict["body"] = body

        if m5:
            req_dict["eventTime"] = formattime(int(m5.group(1)))

    return req_dict


def haiwai_log_assert(req_dict):
    """
    日志断言处理,输出分析结果
    :param req_dict:
    :return:
    """

    # 从 data 中获取日志类型
    if isinstance(req_dict, dict) and req_dict.get("body"):
        if req_dict.get("body").get("data"):
            data_type = req_dict.get("body").get("data").keys()
            data_type_set = set(data_type)
            types_key_set = set(log_type_from_data.keys())
            intersect = data_type_set.intersection(types_key_set)
            if intersect:
                log_type = intersect.pop()
                print ("\033[1;31;40m %s log pass!--from body data || EventTime:-->[%s] \033[0m" % (
                    log_type_from_data.get(log_type), req_dict.get("eventTime")))
                print (req_dict)
            else:
                if 'common' in data_type and len(data_type) == 2:
                    data_type.remove('common')
                    print ("\033[1;31;40m %s log not register!--from body data \033[0m" % data_type)

    # 从 path 中获取日志类型
    path = req_dict.get("path")
    host = req_dict.get("host")
    if host in host_list:
        if path in log_type_from_path.keys():
            eventTime = ""
            if req_dict.get("eventTime"):
                eventTime = req_dict.get("eventTime")
            else:
                if req_dict.get("param"):
                    eventTime = req_dict.get("param").get("time")
                    if eventTime:
                        eventTime = formattime(int(eventTime))
            print ("\033[1;31;40m %s log pass--from url || EventTime:-->[%s] \033[0m" % (
                log_type_from_path.get(path), eventTime))
            print (req_dict)
        elif path and path not in filter_out_list:
            print ("\033[1;31;40m %s log not register!--from url! \033[0m" % path)
            print (req_dict)


def client_log_check(log_type, req_dict, platform="sy"):
    """
    检查SDK客户端请求字段，返回测试结果集
    :param log_type: 日志类型
    :param req_dict: 日志字典
    :param platform: 测试平台
    :return:
    """
    pass


def haiwai_log_case(req_string):
    """
    日志用例集
    一：将数据包转换为dict
    二：对日志分析处理，输出测试结果
    """

    req_dict = req_to_dict(req_string)
    haiwai_log_assert(req_dict)


if __name__ == '__main__':
    try:
        capt_data("eth0", 1)
    except TypeError:
        capt_data("eth0", 1)