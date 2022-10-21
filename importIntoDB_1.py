# _*_ coding : UTF-8 _*_
# @Time : 2022/10/15 23:38
# @Author : GYH
# @File : ImportIntoDB
# @Project :
import json

import pymysql

DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = 'gyh17856973504'
DBNAME = 'zhiHu_data'

flag = int(input('请输入榜单类型(1表示小时榜，2表示日榜，3表示周榜)：'))
if flag == 1:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_hour\\list\\hot_hour_list.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif flag == 2:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_day\\list\\hot_day_list.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)
elif flag == 3:
    with open('E:\\python_learning\\Internet_worm_learning\\reexamine\\zhiHuHot\\hot_week\\list\\hot_week_list.json', 'r', encoding='utf-8') as fp:
        content = fp.read()
    result = json.loads(content)

# print(result)
try:
    # 连接数据库
    DB = pymysql.connect(user=DBUSER, password=DBPASS, host=DBHOST, database=DBNAME, port=3306, charset='utf8')
    print('数据库连接成功!')
    # 创建一个表格
    # 先使用cursor（）方法创建一个游标对象
    cur = DB.cursor()
    if flag == 1:
        # 删除已经存在且同名的关系表格
        cur.execute('DROP TABLE IF EXISTS hour_dataList')
        # 创建表格
        sql = 'CREATE TABLE hour_dataList(Topics CHAR(70), Title CHAR(55), Url CHAR(40), Score FLOAT(6), New_follow_num INT, New_answer_num INT, New_upvote_num INT)'
        cur.execute(sql)
        print('表格创建成功!')
    elif flag == 2:
        # 删除已经存在且同名的关系表格
        cur.execute('DROP TABLE IF EXISTS day_dataList')
        # 创建表格
        sql = 'CREATE TABLE day_dataList(Topics CHAR(70), Title CHAR(55), Url CHAR(40), Score FLOAT(6), New_follow_num INT, New_answer_num INT, New_upvote_num INT)'
        cur.execute(sql)
        print('表格创建成功!')
    elif flag == 3:
        # 删除已经存在且同名的关系表格
        cur.execute('DROP TABLE IF EXISTS week_dataList')
        # 创建表格
        sql = 'CREATE TABLE week_dataList(Topics CHAR(70), Title CHAR(55), Url CHAR(40), Score FLOAT(6), New_follow_num INT, New_answer_num INT, New_upvote_num INT)'
        cur.execute(sql)
        print('表格创建成功!')
    # 添加数据：
    i = 0
    while i < len(result):
        if flag == 1:
            sql = 'INSERT INTO hour_dataList(Topics, Title, Url, Score, New_follow_num, New_answer_num, New_upvote_num) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        elif flag == 2:
            sql = 'INSERT INTO day_dataList(Topics, Title, Url, Score, New_follow_num, New_answer_num, New_upvote_num) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        elif flag == 3:
            sql = 'INSERT INTO week_dataList(Topics, Title, Url, Score, New_follow_num, New_answer_num, New_upvote_num) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        values = (result[i]['topics'], result[i]['title'], result[i]['url'], result[i]['score'], result[i]['new_follow_num'], result[i]['new_answer_num'], result[i]['new_upvote_num'])
        cur.execute(sql, values)
        DB.commit()
        print('数据插入成功!')
        i = i + 1
except pymysql.Error as error:
    print('数据库连接失败或表格创建失败：' + str(error))
    DB.rollback()

