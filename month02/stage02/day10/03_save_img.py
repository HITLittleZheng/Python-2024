"""
数据库存取文件
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

# 添加图片
# with open("pyy.jpeg",'rb') as fr:
#     data = fr.read()
# sql="update class set image=%s where id=1;"
# cur.execute(sql,[data])
# db.commit()

# 取出图片
sql="select name,image from class where id=1;"
cur.execute(sql)
name,image = cur.fetchone() # (name,image)
with open(name+".jpeg",'wb') as fw:
    fw.write(image)

# 关闭
cur.close()
db.close()
