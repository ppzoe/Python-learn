import logging
import time

import pymysql
import requests
from datetime import datetime

cookie = "SINAGLOBAL=9647412095234.6.1640246418846; UOR=www.baidu.com,weibo.com,www.baidu.com; SL_G_WPT_TO=zh; XSRF-TOKEN=gQuhF_75Ipqh5i-Laiw-MCZ6; SSOLoginState=1655426349; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; _s_tentry=weibo.com; Apache=2841001404702.55.1655694166607; ULV=1655694166620:12:5:2:2841001404702.55.1655694166607:1655091898985; PC_TOKEN=4c215c9d42; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF01YMUE2SQUse1CbGJT33q5JpX5KMhUgL.FozXeh2fSh.fSh-2dJLoI0qLxK-LBo.LBoeLxKqLBoMLBK2LxKBLBonLBoqLxK-L12qL1hnLxK-LBKqL1hzLxKBLB.BL1K-t; ALF=1687307360; SCF=AguY-Aj-Uaa6bVkTQCb9K5idnPXvJY2CmhVzApDg1Yb39oh4QsiT6AWVI0UWIKX5S6ibiZ_v5XRmatr7QglE1zg.; SUB=_2A25PtWCwDeRhGeRK61MU9CfJzzmIHXVsw9V4rDV8PUNbmtB-LVLRkW9NU3tst1lfMTVWwsOc-D0Gh-TqJSCDNwhJ; WBPSESS=fLtleuy1hZ_tMMSUlLky_guMBFx5g9XNCfQekiz42ZytU-PpQSiutZ1J6yxdxoR15af62BCJ_zTIIhhHc1i-7VnpaVIvsTq8LvA88bfNh0ype7lz3hD7vL3Ig0ese3pOKbr6qPG9EGFkE_Ouqkuhbw=="
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    "cookie": cookie
}
# 字典 查询微博对应uid
wb_data_dic = {}
wb_data_list = []
# wbid = {"吉林检察": "5093990523", "辽源西安检察": "5395116343", "公主岭检察": "5584068981"}
wbid = {"扶余检察": "6385694129", "洮北检察": "5852251873"}


def con():
    # 数据存储
    conn = pymysql.connect(host="localhost", user="root", password="root123456", db='weibo')
    cursor = conn.cursor()
    sql = """
            INSERT INTO weibo_data1(name,fans_num,base_url,url,content,relay_num,comment_num,like_num,is_original,uid,send_time)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,str_to_date(%s,"%%Y-%%m-%%d %%H:%%i:%%s"))
            """
    try:
        # # 执行SQL语句 ,提交单行数据
        # cursor.execute(sql, w2)
        # 执行SQL语句 ,提交多行数据
        cursor.executemany(
            sql, wb_data_list
        )
        # 提交事务到数据库执行
        conn.commit()  # 事务是访问和更新数据库的一个程序执行单元
        print("存储成功！！！！")
    except Exception as e:
        # 如果发生错误则执行回滚操作
        print(e)
        conn.rollback()
        print("回滚，存储失败")
    finally:
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()
        # exit()  # 退出数据监控


def wb_home_data(userid, headers):
    global screen_name, followers_count, url
    url = "https://weibo.com/ajax/profile/info?custom=" + userid
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
    # # verified_reason 验证原因
    # verified_reason = wbhome_dic["data"]["user"]["verified_reason"]
    # location 位置，所在地
    location = wbhome_dic["data"]["user"]["location"]
    print("微博名称： " + str(screen_name))
    print("粉丝数： " + str(followers_count))
    print("粉丝数简写： " + str(followers_count_str))
    print("微博号识别标识： " + str(uid))
    # print("验证原因： " + str(verified_reason))
    print("位置，所在地： " + str(location))
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    wbhome.close()
    return screen_name, followers_count, url


def wb_Every_data(uid, stat, headers):
    for page in range(1, 50, 1):
        time.sleep(0.05)
        urls = "https://weibo.com/ajax/statuses/mymblog?uid=" + str(uid) + "&page=" + str(
            page) + "&feature=0&stat_date=" + str(stat)
        # wb = requests.get(urls, headers=headers)
        for i in range(10):
            wb = requests.get(urls, headers=headers)
            if wb.status_code != 200:
                time.sleep(15)
                logging.info("Checking Response Status Code again")
                continue
            elif wb.status_code == 200:
                wb.encoding = "utf-8"
                dic = wb.json()
                break
        try:
            for i in range(20):

                # reads_count 阅读数
                reads_count = dic['data']['list'][i]['reads_count']
                # reposts_count 转发数
                reposts_count = dic['data']['list'][i]['reposts_count']
                # screen_name_suffix_new 有此条目表示快转
                # attitudes_status 有此条目表示转发
                if dic['data']['list'][i].get('screen_name_suffix_new') or dic['data']['list'][i].get(
                        'attitudes_status') in dic['data']['list'][i]:
                    r_type = False  # r_type 是否为原创微博
                else:
                    r_type = True
                # retweeted_status 转发原微博的数据列表
                # retweeted_status = dic['data']['list'][0]['reads_count']
                # created_at 发布时间
                created_at = dic['data']['list'][i]['created_at']
                gmt_format = '%a %b %d %H:%M:%S +0800 %Y'
                send_time = datetime.strptime(created_at, gmt_format)  # GMT时间格式 转 datetime时间格式
                # comments_count 评论数
                comments_count = dic['data']['list'][i]['comments_count']
                # attitudes_count 点赞数
                attitudes_count = dic['data']['list'][i]['attitudes_count']
                # id  文章id 定义为变量 wid
                wid = dic['data']['list'][i]['id']
                # mblogid 移动博客id  微博网址+uid+mblogid == 此条微博的地址 wurl
                mblogid = dic['data']['list'][i]['mblogid']
                wurl = "https://weibo.com/" + str(uid) + "/" + str(mblogid)
                # text_raw 微博内容
                text_raw = dic['data']['list'][i]['text_raw']

                # df = pd.DataFrame(dic['data']['list'])
                # mydic = dic['data']
                print("阅读数: " + str(reads_count))
                print("转发数: " + str(reposts_count))
                print("转发类型: " + str(r_type))
                print("发布时间: " + str(created_at))
                print("评论数: " + str(comments_count))
                print("点赞数: " + str(attitudes_count))
                print("文章id: " + str(wid))
                print("移动博客id: " + str(mblogid))
                print(wurl)
                print("内容: " + str(text_raw))
                print("完成此微博页第" + str(i + 1) + "条信息统计")
                wb_data_list.append((screen_name, followers_count, url, wurl, text_raw, reposts_count,
                                     comments_count, attitudes_count, r_type, uid, send_time))
                # print(wb_data_list)
                print("完成此微博第" + str(page) + "页信息统计")
                print("=====================================================================")
        except IndexError:
            print("完成此微博第" + str(page) + "页信息统计")
            print("----------------------------------------------------------------------------")
            continue
        except Exception as e:
            print(e)
            print(repr(e))
            break
        finally:
            wb.close()

    return wb_data_list.append


if __name__ == '__main__':
    # stat 需要查询的年月范围
    stat = "202205"
    for key in wbid:
        userid = wbid[key]
        wb_home_data(userid, headers)
        # print(wb_data_list)
        wb_Every_data(userid, stat, headers)
        con()  # def 缓存列表，上传到数据库
        time.sleep(0.1)
        wb_data_list.clear()  # 清理缓存列表
