import pymysql
import logging

class MySQLCommand(object):
    def __init__(self,host,port,user,passwd,db,table):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.db = db
        self.table = table

    def connectMysql(self):
        try:
            self.conn=pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.password
                                        ,db=self.db,charset='gbk')
            self.cursor = self.conn.cursor()
        except:
            print('error')

    def queryMysqlById(self,id):
        sql = "SELECT * FROM " + self.table +" where id="+str(id)+" order by id desc;"

        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            print(row)
            return row
        except:
            print(sql + ' execute failed.')
            return ""

    def insertMysql(self,name,age,grade):
        sql = "INSERT INTO " + self.table + "(name,age,grade) VALUES('" + name + "'," + age + "," + grade + ")"
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            print("insert failed.")

    def updateMysqlSN(self,id,age,grade):
        sql = "UPDATE " + self.table + " SET age=" + age + ",grade="+ grade + " WHERE id=" + id
        print("update sn:" + sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()


    def closeMysql(self):
        self.cursor.close()
        self.conn.close()

        




