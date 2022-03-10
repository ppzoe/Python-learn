from unittest import result

import pymysql

conn = pymysql.connect(host="36.138.58.148", user="root", password="1qaz@WSXsht")
# db="sht-sgne" 连接数据库
conn.select_db('sht-sgne')
#获取游标
cur=conn.cursor()

cur.execute("select * from fin_recharge;")
while 1:
    res=cur.fetchone()
    if res is None:
        #表示已经取完结果集
        break
    print (res)
cur.close()
conn.commit()
conn.close()
print('sql执行成功')