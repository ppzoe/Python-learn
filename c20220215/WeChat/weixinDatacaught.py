from mitmproxy import http, ctx
import json
import pymysql
from urllib.parse import quote, unquote
import time
import datetime


def b(l_text):  # biz解析
    for i in l_text:
        if "__biz=" in i:
            l1_text = i
            BIZ = l1_text[6:]
            biz_1 = (unquote(BIZ, 'utf-8'))
            return biz_1


def ct_s(l_text):  # ct解析
    for i in l_text:
        if "ct=" in i:
            l1_text = i
            ct1 = l1_text[3:]
            ct = int(ct1)
            timeArray = time.localtime(ct)
            c2 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            c3 = datetime.datetime.strptime(c2, "%Y-%m-%d %H:%M:%S")
            return c3


def title(l_text):  # 标题解析
    for i in l_text:
        if "title=" in i:
            l1_text = i
            t_ed = l1_text[6:]
            ti_ed = (unquote(t_ed, 'utf-8'))
            titled = (unquote(ti_ed, "utf-8"))
            return titled


def response(flow: http.HTTPFlow) -> None:
    if "mp.weixin.qq.com/mp/getappmsgext" in flow.request.url:  # 抓取微信数据返回字段,post请求
        json_text = json.loads(flow.response.text)              # json格式截取回响正文
        json_read = json_text['appmsgstat'].get("read_num")     # 解析目标数据 阅读数,点赞数据,取消点赞
        json_like = json_text['appmsgstat'].get('like_num')
        json_old_like = json_text['appmsgstat'].get('old_like_num')
        json_request_text = flow.request.get_text()
        print(json_like, json_read, json_old_like)
        print("获取成功正在存储")
        # with open('data.json', 'w') as f:
        #     json.dump(flow.response.text, f)
        l_text = json_request_text.split('&')   # 字符串解析,提取解析请求头数据
        biz = b(l_text)
        titled = title(l_text)
        ct = ct_s(l_text)

        # 数据存储
        conn = pymysql.connect(host="124.70.0.180", user="root", password="Root@1234.", db='jlrmt')
        cursor = conn.cursor()

        # 数据库字段与微信字段名称有所出入，read_num 阅读数 ，like_num 微信为old_like_num 点赞数，biz 用来识别微信公众号，title文字名称，
        # create_time文章发布时间，look_num 微信为 like_num 再看数 注意与点赞的区分
        sql = "INSERT INTO man_wx_data(read_num,like_num,look_num,biz,title,create_time)VALUES (%s,%s,%s,'%s','%s'," \
              "str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'))" % \
              (json_read, json_old_like, json_like, biz, titled, ct)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交事务到数据库执行
            conn.commit()  # 事务是访问和更新数据库的一个程序执行单元
            print("存储成功！！！！")
        except:
            # 如果发生错误则执行回滚操作
            conn.rollback()
            print("回滚，存储失败")
        # 关闭游标
        cursor.close()
        # 关闭数据库连接
        conn.close()
        exit()  # 退出数据监控


addons = [response]
