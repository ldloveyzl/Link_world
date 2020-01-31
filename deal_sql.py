import pymysql
import hashlib
import deal_sql

# 传入一个密码返回加密后的密码
def change_passwd(passwd):
    hash = hashlib.md5()  # md5对象
    hash.update(passwd.encode())  # 加密
    return hash.hexdigest()


class Database:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='chat',
                                  charset='utf8')

        # 生成游标对象 (操作数据库,执行sql语句,获取结果)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库连接
        self.cur.close()
        self.db.close()

    def register(self, name, passwd):
        sql = "select name from user where name='%s';" % name
        self.cur.execute(sql)
        # 如果查到内容返回False
        if self.cur.fetchone():
            return False
        # 插入数据库
        sql = "insert into user (name,pwd) values (%s,%s);"
        passwd = change_passwd(passwd)  # 密码加密
        self.cur.execute(sql, [name, passwd])
        self.db.commit()
        return True
        # try:
        #     self.cur.execute(sql, [name, passwd])
        #     self.db.commit()
        #     return True
        # except:
        #     self.db.rollback()
        #     return False

    def login(self, name, pwd):
        sql = "select name from user " \
              "where name=%s and pwd=%s;"
        pwd = change_passwd(pwd)
        self.cur.execute(sql, [name, pwd])
        if self.cur.fetchone():
            return True
    def getfriends(self,name):
        sql="select frie from friend where name=%s;"
        self.cur.execute(sql,name)
        friends=self.cur.fetchall()
        print(friends)
    def query(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        r = self.cur.fetchone()
        # r->(xxx,)  None
        if r:
            return r[0]

    def insert_history(self, name, word):
        # id  name word time
        sql = "insert into hist2 (name,word) values (%s,%s);"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except:
            self.db.rollback()

    def history(self, name):
        sql = "select name,word,time " \
              "from hist2 " \
              "where name=%s " \
              "order by time desc limit 10;"
        self.cur.execute(sql, [name])
        return self.cur.fetchall()


if __name__ == '__main__':
    db = Database()
    db.register('ldloveyzl', 'lmjlove1230')
    # db.login('Tom', '123')
    db.close()
