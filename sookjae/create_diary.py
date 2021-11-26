import sookjae.dao as dao
vo=list()
title = input('타이틀 ')
vo.append(title)
content = input('내용 ')
vo.append(content)
create = dao.DAO()
create.create(vo)