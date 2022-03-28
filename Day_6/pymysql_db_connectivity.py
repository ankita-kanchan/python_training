import pymysql as py
import datetime
#connect database
#hostname,user,password,database
db = py.connect(host="localhost",user="root",password="kira",database="python_training")

#cusror object for database
cur = db.cursor()

# add data in user table
#name, email_id, contact, password, created
q="insert into user values(%s,%s,%s,%s,%s,%s)"
values=[0,"john doe","john@gmail.com","1234567890","John@123",datetime.datetime.now()]
cur.execute(q,values)

db.commit()

#fetching data from table

#select  * from table_name

q="select name,email_id from user"
cur.execute(q) #resultset
data = cur.fetchall() #multiple records
print(data)

q="select name,email_id from user"
cur.execute(q) #resultset
data = cur.fetchone() #single record
print(data)

id=2
q="select name,email_id from user where id=%s"
cur.execute(q,[id]) #resultset
data = cur.fetchone() #single record
print(data)

#Update record from table
# update table_name set column_name=new value where condition
q="update user set name=%s where id =%s"
values=["Jake Doe",2]

cur.execute(q,values)

db.commit()

#Delete record from table
#Delete from table where condition
q="delete from user where id=%s"
values=[2]
cur.execute(q,values)
db.commit()









