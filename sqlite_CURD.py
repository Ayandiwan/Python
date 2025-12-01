import os
os.chdir("E:\Sem5\Python\db")

import sqlite3

conn = sqlite3.connect('db2.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM ad;")


records = cursor.fetchall()


for record in records:
    print(record)
    
conn.close()







import sqlite3
conn = sqlite3.connect("ad.db")

cursor = conn.cursor()
query = f"INSERT INTO 'ad'VALUES (18, 'SURYA', 'TARAPUR',20)"
cursor.execute(query)
conn.commit()
conn.close()




import sqlite3
roll_to_search = int(input("Enter the roll number to search: "))
conn = sqlite3.connect("db2.db")
cursor = conn.cursor()
search_query = f"SELECT * FROM ad WHERE id ={roll_to_search}"
#search_query = f"SELECT * FROM Pupil"
cursor.execute(search_query)
row = cursor.fetchone()
#row = cursor.fetchall()
print(row)




import sqlite3
conn = sqlite3.connect("db2.db")
cursor = conn.cursor()
roll_to_delete = int(input("Enter the roll number to delete: "))
delete_query = f"DELETE FROM ad WHERE id = {roll_to_delete}"
cursor.execute(delete_query)
if cursor.rowcount > 0:
 print(f"Record with id = {roll_to_delete} deleted successfully!")
else:
 print(f"No record found with id ={roll_to_delete}")
conn.commit()
conn.close()


