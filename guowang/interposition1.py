import random
import time
import pymysql


class DatabaseAccess():
    # 初始化属性
    def __init__(self):
        self.__db_host = "36.138.58.148"
        self.__db_port = 3306
        self.__db_user = "root"
        self.__db_password = "1qaz@WSXsht"
        self.__db_database = "sht-sgne"

    # 链接数据库
    def isConnectionOpen(self):
        self.__db = pymysql.connect(
            host=self.__db_host,
            port=self.__db_port,
            user=self.__db_user,
            password=self.__db_password,
            database=self.__db_database,
            charset='utf8'
        )


    # 插入数据
    def linesinsert(self, recharge_id,amount,status,user_id,phonenumber,channel,del_flag,create_time,remark):
        try:
            # 连接数据库
            self.isConnectionOpen()
            # 创建游标
            global cursor
            cursor = self.__db.cursor()
            # sql命令
            sql = """INSERT INTO fin_recharge(recharge_id,amount,status,user_id,phonenumber,channel,del_flag,create_time,remark)
                VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (recharge_id, amount, 0, 125347893, 13341435789, channel, 0, c_time, 2016081621001004400236957647)
            # 执行sql命令
            cursor.execute(sql)
        except Exception as e:
            self.__db.rollback()
            print(e)
        finally:
            # 关闭游标
            cursor.close()
            # 提交
            self.__db.commit()
            # 关闭数据库连接
            self.__db.close()

    # 数据生成，姓名，年龄，并调用数据插入方法
    #  生成订单号
    def get_order_code(self):
        #  年月日时分秒+time.time()的后5位
        order_no = str(
            time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + str(time.time()).replace('.', '')[-5:])
        return order_no
    # 随机一个recharge_id
    recharge_id = get_order_code()
    def data_update(self):

        # 随机选取支付渠道
        zf = ["支付宝", "微信"]
        random.choice(zf)
        channel = (random.choice(zf))

        # 随机选取支付金额
        je = [80.00, 100.00, 200.00, 68.00, 12.00, 88.00]
        random.choice(je)
        amount = random.choice(je)

        # 随机选取支付时间
        a1 = (2019, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组(2019-01-01 00：00：00)
        a2 = (2021, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组(2021-12-31 23：59：59)
        start = time.mktime(a1)  # 生成开始时间戳
        end = time.mktime(a2)  # 生成结束时间戳

        # 随机生成10个日期字符串
        for i in range(10):
            t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t)  # 将时间戳生成时间元组
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串(1976-05-21)
        self.linesinsert(recharge_id,amount,status,user_id,phonenumber,channel,del_flag,create_time,remark)


if __name__ == "__main__":
    # 创建实例化对象
    db = DatabaseAccess()
    # 循环100次，插入100条数据
    for record in range(1, 2):
        # 调用方法
        db.data_update()
