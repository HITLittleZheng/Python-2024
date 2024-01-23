"""
数据库读操作  select
"""
import pymysql

# 参数字典
kwargs = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "stu",
    "charset": "utf8"
}
# 连接数据库
db = pymysql.connect(**kwargs)

# 生成游标: 执行sql操作数据，得到操作结果的对象
cur = db.cursor()

# 数据读取操作
sql="select name,score from class where score>%s;"
cur.execute(sql,[80])

# 获取查询结果
# one = cur.fetchone() # None
# print(one)
#
# many = cur.fetchmany(2) # ()
# print(many)
#
# all = cur.fetchall() # ()
# print(all)

# 迭代取值
for row in cur:
    print(row)



# 关闭
cur.close()
db.close()
