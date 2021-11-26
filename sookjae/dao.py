import pymysql

class DAO():
    # id = 0
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306,
                               user='root', password='1234',
                               db='cloth', charset='utf8')
        self.cur=self.conn.cursor()
    def create(self,vo):

        sql='insert into diary values (null, now(), %s,%s)'
        result = self.cur.execute(sql, vo)
        print('확인', result)
        self.conn.commit()
        self.conn.close()

    def read(self):
        sql='select * from diary'
        result = self.cur.execute(sql)
        # print('확인', result)
        rows = self.cur.fetchall()
        for i in rows:
            print(i)
        self.conn.commit()
        self.conn.close()
        return rows
    def update(self,vo,id):

        sql=f'update diary set title= %s, content = %s where id= {id}'
        result= self.cur.execute(sql, vo)
        print('확인', result)
        self.conn.commit()
        self.conn.close()

    def delete(self, id):

        sql='delete from diary where id= %s'
        result = self.cur.execute(sql, id)
        print('확인',result)
        self.conn.commit()
        self.conn.close()

