import sookjae.dao as dao
vo = list()
id= int(input('id '))
title = input('타이틀(수정) ')
vo.append(title)
content = input('내용(수정) ')
vo.append(content)
read = dao.Dao()
read.update(vo,id)