"""
根据逻辑处理需要，提供数据支持
"""
import pymysql
import hashlib

# 密码加密
def change_passwd(passwd):
    hash = hashlib.sha256()
    hash.update(passwd.encode())
    return hash.hexdigest()


class Dict:
    def __init__(self):
        self.kwargs = {
            "user": "root",
            "password": "123456",
            "database": "dict",
            "charset": "utf8"
        }
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    # 　注册验证
    def register(self, name, passwd):
        passwd = change_passwd(passwd)
        sql = "insert into user (name,password) values (%s,%s);"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False

    # 　处理登录
    def login(self, name, passwd):
        passwd = change_passwd(passwd)
        sql = "select id from user where binary name=%s and password=%s;"
        self.cur.execute(sql, [name, passwd])
        # (id,)  None
        if self.cur.fetchone():
            return True
        else:
            return False

    # 查询单词
    def query(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        return self.cur.fetchone()  # (mean,) None

    def insert_hist(self, name, word):
        # id  user_id  words_id  time
        sql = "select id from user where name=%s;"
        self.cur.execute(sql, [name])
        user_id = self.cur.fetchone()[0]
        sql = "select id from words where word=%s;"
        self.cur.execute(sql, [word])
        words_id = self.cur.fetchone()[0]
        sql = "insert into hist (user_id,words_id) values (%s,%s);"
        self.cur.execute(sql, [user_id, words_id])
        self.db.commit()

    def hist(self, name):
        # name  word  time--> user_id words_id time
        sql = "select name,word,time " \
              "from user inner join hist " \
              "on user.id=hist.user_id " \
              "inner join words " \
              "on words.id=hist.words_id " \
              "where name=%s " \
              "order by time desc " \
              "limit 10;"
        self.cur.execute(sql, [name])
        return self.cur.fetchall()  # () ((),)
