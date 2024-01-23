"""
数据库的连接与关闭
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

# 数据操作


# 关闭
cur.close()
db.close()
