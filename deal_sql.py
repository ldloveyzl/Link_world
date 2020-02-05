import time

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

    def login(self, name, pwd, addr):
        sql = "select name from user " \
              "where name=%s and pwd=%s;"
        pwd = change_passwd(pwd)
        self.cur.execute(sql, [name, pwd])
        if self.cur.fetchone():
            sql = "update user set addr=%s,port=%s where name=%s"
            try:
                self.cur.execute(sql, [addr[0], addr[1], name])
                self.db.commit()
            except Exception as e:
                print(e)
                self.db.rollback()
                return
            return True

    def getfriends(self, name):
        sql = "select frie from friend where name=%s;"
        self.cur.execute(sql, name)
        str1 = ''
        friends = self.cur.fetchall()
        for i in friends:
            str1 += " " + i[0]
        print(str1)
        return str1.strip()

    def get_friend_addr(self, friend):
        sql = "select addr,port from user where name = %s"
        self.cur.execute(sql, friend)
        fake_addr = self.cur.fetchone()
        addr = fake_addr[0]
        port = int(fake_addr[1])
        return addr, port

    def save_msg(self, name, friend, msg):
        sql = "insert into chat_his (sender,rever,record) values (%s,%s,%s);"
        try:
            self.cur.execute(sql, [name, friend, msg])
            self.db.commit()
        except Exception as e:
            print('error',e)
            self.db.rollback()

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
    # db.register('ldloveyzl', 'lmjlove1230')
    db.getfriends('uu')
    # db.login('Tom', '123')
    db.close()
