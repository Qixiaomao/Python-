# MySQL
import pymysql

'''
db = pymysql.connect(host='localhost',user='root',passwd='12345678',port=3306,db='spiders')
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:',data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY (id))'
cursor.execute(sql)
db.close()

'''

# 插入数据

data = {
    "id":"20230102",
    "user":"Sam",
    "age":22
}
table = 'students'
keys =','.join(data.keys())
values = ','.join(['%s']*len(data))
sql = 'insert into {table}({keys}) values({values})'.format(table=table,keys=keys,values=values)
update = ','.join(["{key}=%s".format(key=key) for key in data])
sql += update

db = pymysql.connect(host='localhost',port=3306,db='spiders',user='root',passwd='12345678')
cursor = db.cursor()


try:
    if cursor.execute(sql,tuple(data.values())*2):
       print('Successful!')
       db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
    