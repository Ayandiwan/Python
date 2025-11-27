import sqlite3 


conn=sqlite3.connect("i1.db")

cursor=conn.cursor()

cursor.execute("SELECT*FROM ad")



records=cursor.fetchall()


for rec in records:
    print(rec)



cursor.execute("SELECT SUM(Bill_Amount) FROM ad")


for i in cursor.fetchone():
    print("Total",i)

    
conn.close()    





