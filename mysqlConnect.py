import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Testing!6", database = 'pythonclass')

# print(dir(mydb))
mycursor = mydb.cursor()
mycursor.execute('select * from student where address = "medavakkam"')
# sql = 'insert into student (name, address) values (%s ,%s)'
# values = ('abc', 'sithalapakkam')
# mycursor.execute(sql, values)
# print(mycursor.rowcount, 'rows inserted')
# mydb.commit()
result = mycursor.fetchall()
for i in result:
  print(i)
