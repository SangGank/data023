import db_test.dao
li=list()
id= input('id>> ')
li.append(id)
pw= input('pw>> ')
li.append(pw)
name= input('name>> ')
li.append(name)
tel= input('tel>> ')
li.append(tel)
# print(li)
# 값을 전달할 때 묶어서 보내는 역할의 클래스(data transfer object, DTO, value Object, VO)
# list를 선호
# db_test.dao.create(id, pw, name, tel)
db_test.dao.create(li)


vo=list()
vo.append(id)
vo.append(pw)
vo.append(tel)

db_test.dao.update(vo)

db_test.dao.delete(id)


