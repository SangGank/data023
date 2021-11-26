import pymysql
conn = pymysql.connect(host='localhost', port=3306,
                       user = 'root', password='1234',db='cloth', charset = 'utf8')

print('db연결 성공', conn)