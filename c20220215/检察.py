import MySQLdb
import xlrd2
# 设置变量存储失败数据
weixin_Failuredata = []
weibo_Failuredata = []


def con_weibo(uid, day):
    # 打开数据库连接
    db = MySQLdb.connect("124.70.0.180", "root", "Root@1234.", "jlrmt", charset='utf8mb4')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select count(*) from man_weibo_data where uid = '" + uid + "' and left(send_time,7) ='" + day + "'"

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            # 打印结果
            print(row[0])
            if row[0] == 0:
                weibo_Failuredata.append(uid)
                print("失败用户" + uid)
    except:
        print("Error: unable to fecth data")
    # 关闭数据库连接
    db.close()


def con_wechat(biz, day):
    # 打开数据库连接
    db = MySQLdb.connect("124.70.0.180", "root", "Root@1234.", "jlrmt", charset='utf8mb4')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select COUNT(*) from man_wx_data where biz='" + biz + "' and left(create_time,7) = '" + day + "'"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            # 打印结果
            print(row[0])
            if row[0] == 0:
                weixin_Failuredata.append(biz)
                print("失败用户" + biz)
    except Exception as e:
        print(e)
        print("Error: unable to fecth data")
    # 关闭数据库连接
    db.close()


def Qu_Failuredata(day):
    # 打开excel
    wb = xlrd2.open_workbook('sys_dept.xlsx')
    # 按工作簿定位工作表
    sh = wb.sheet_by_name('sys_dept')
    # biz
    biz = sh.col_values(1)
    uid = sh.col_values(2)
    print(biz)  # 输出第一行的所有值
    print(uid)  # 输出第二行的所有值
    print(type(uid))
    # # 遍历excel，打印所有数据
    # for i in range(sh.nrows):
    #     print(sh.row_values(i))
    for i in range(len(biz)):
        print(i+1, biz[i])
        con_wechat(biz[i], day)
    for i in range(len(uid)):
        print(i+1, int(uid[i]))
        con_weibo(str(int(uid[i])), day)

    print(weixin_Failuredata)
    print(weibo_Failuredata)


if __name__ == '__main__':
    print("请输入查询月份 如：2022-10")
    day = input()
    Qu_Failuredata(day)



# select count(*) from man_weibo_data where uid = '5584068981' and left(send_time,7) ='2022-09'
# select COUNT(*) from man_wx_data where biz='MzAwMjc0OTcxNA==' and left(create_time,7) = '2022-09'
