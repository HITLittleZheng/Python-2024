"""
数据库写操作示例　insert delete update

对数据库写操作会默认开启事务，如果数据表
支持事务需要commit提交才能生效，如果数据表
不支持事务则execute执行语句后立即生效
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

# 数据写操作
try:
    # sql="update class set score=%s where name=%s;"
    # cur.execute(sql,[99,"Lily"]) # 给sql语句传值
    # sql="delete from class where score<%s;"
    # cur.execute(sql,[60])

    #　批量操作
    data = [("zhang",16,'m',70),
            ("wang",17,'w',71),
            ("lisi",18,'m',72)]
    sql="insert into class (name,age,sex,score) " \
        "values (%s,%s,%s,%s);"
    cur.executemany(sql,data)
except Exception as e:
    print(e)
    db.rollback() # 事务回滚
else:
    db.commit() #　提交事务


# 关闭
cur.close()
db.close()
