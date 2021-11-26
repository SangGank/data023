import db.dao as dao

# id= input('id  ')
rows =dao.all()

print('---------------------------')
# print(f'결과는 {row[0]} {row[1]} {row[2]} {row[3]}')

for row in rows:
    # print(i)
    print(f'결과는 {row[0]} {row[1]} {row[2]} {row[3]}')

for one in range(len(rows)):
    print(rows[one])

# 모듈을 만들 때는 각자의 역할에 충실하도록, 역할을 섞어서 만들면 안된다.
# 응집도