# encoding: utf-8
# @author: will
# @file: mysql开发.py
# @time: 2022/8/13 10:50
from dbmysql import DbMysql
# SQL开发1
# if __name__ == '__main__':
#     # 连接数据库
#     db = DbMysql(host='localhost',user='root',password='will0616',database="hive",charset='utf8')
#     # 查询
#     datas = db.find('select * from exam_record')
#     print(datas[:2])


# SQL开发2
import pymysql
import mysql.connector
# try:
#     con = pymysql.connect(host='localhost',user='root',password='will0616',database='ershua')
#     # 开启事物
#     con.start_tr