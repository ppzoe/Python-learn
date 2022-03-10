# coding:utf-8
import pymysql
import time
import random
from decimal import Decimal


#  生成订单号
def get_order_code():
    #  年月日时分秒+time.time()的后5位
    order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + str(time.time()).replace('.', '')[-5:])
    return order_no


# 打开数据库连接
conn = pymysql.connect(host="36.138.58.148", user="root", password="1qaz@WSXsht", db='sht-sgne')
for i in range(2):  # 循环次数
    # 使用cursor()方法获取操作游标
    cursor = conn.cursor()

    # 随机一个recharge_id
    recharge_id = get_order_code()
    # 随机选取支付渠道
    zf = ["支付宝", "微信"]
    random.choice(zf)
    channel = (random.choice(zf))

    # 随机选取支付金额
    je = random.uniform(60, 200)
    amount = Decimal(je).quantize(Decimal('0.00'))

    # 随机选取支付时间
    a1 = (2019, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组(2019-01-01 00：00：00)
    a2 = (2021, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组(2021-12-31 23：59：59)
    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳

    # 随机生成10个日期字符串
    for i in range(1):
        t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    c_time = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串(1976-05-21)

    # SQL语句：向数据表中插入数据

    time.sleep(1)  # 执行语句等待1秒
    try:
        sql = """INSERT INTO fin_recharge(recharge_id,amount,status,user_id,phonenumber,channel,del_flag,create_time,remark)
            VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            recharge_id, amount, 0, 125347893, 13341435789, channel, 0, c_time, 2016081621001004400236957647)
        # 执行SQL语句
        cursor.execute(sql)
        # 提交事务到数据库执行
        conn.commit()  # 事务是访问和更新数据库的一个程序执行单元
    except:
        # 如果发生错误则执行回滚操作
        conn.rollback()

# 查询添加后数据库数据
cursor.execute("select * from fin_recharge;")
print('修改后的数据为：')
for res in cursor.fetchall():
    print(res)
print('*' * 40)
# 关闭游标
cursor.close()
# 关闭数据库连接
conn.close()




