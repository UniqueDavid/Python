import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()
cursor.execute('select * from user where id=?',(1,))
print(cursor.fetchall())
cursor.close()
conn.close()