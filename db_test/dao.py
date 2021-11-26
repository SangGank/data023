import pymysql
# def create(id, pw, name, tel):

def create(li):
    # id= li[0]
    # pw=li[1]
    # name =li[2]
    # tel=li[3]

    conn = pymysql.connect(host='localhost', port=3306,
                           user = 'root', password='1234',
                           db='cloth', charset = 'utf8')

    print('1. db연결 성공', conn)

    cur = conn.cursor()
    print('2. db연결 스트림을 접근할 수 있는 객체 획득 성공', cur)

    # sql=f'insert into member values ({id},{pw},{name},{tel})'
    # sql="insert into member values ('" + id +"','" + pw + "','" + name + "','" + tel + "')"
    # sql="insert into member values ('" + li[0] +"','" + li[1] + "','" + li[2] + "','" + li[2] + "')"
    sql ='insert into member values (%s,%s,%s,%s)'
    result=cur.execute(sql, li)
    # result = cur.execute(sql)
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)
    conn.commit()
    conn.close()
def delete(id):
    conn = pymysql.connect(host='localhost', port=3306,
                           user = 'root', password='1234',
                           db='cloth', charset = 'utf8')
    cur= conn.cursor()
    sql = 'delete from member where id = %s'
    result =cur.execute(sql,id)
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)
    conn.commit()
    conn.close()

def update(vo):
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', password='1234',
                           db='cloth', charset='utf8')
    cur = conn.cursor()
    sql = 'update member set tel= %s, pw =%s where id = %s'
    vo2=[vo[2],vo[1],vo[0]]
    result = cur.execute(sql, vo2)
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)
    conn.commit()
    conn.close()


def read(id):
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', password='1234',
                           db='cloth', charset='utf8')
    cur = conn.cursor()
    sql = 'select * from member where id = %s'

    result = cur.execute(sql, id)

    row = cur.fetchone()

    print(row)
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)
    conn.commit()
    conn.close()
    return row

def all():
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', password='1234',
                           db='cloth', charset='utf8')
    cur = conn.cursor()
    sql = 'select * from member'

    result = cur.execute(sql)

    rows = cur.fetchall()

    print(len(rows))
    print(rows)
    print('3. sql문을 만들어서 mysql로 보낸 후 결과값>> ', result)
    conn.commit()
    conn.close()
    return rows

# 해당 모듈이 main이 되어서 실행될때만, 실행해 주는 부분...!
if __name__ == '__main__':
    create('apple','apple','apple','apple')