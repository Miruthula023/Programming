import sqlite3

connection = sqlite3.connect("organis.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE Employee(Eno integer,EmpName char(20),Esal integer,Dept char(20));""")
cursor.execute("""INSERT INTO Employee VALUES(3,'XXXXX',45000,'IT');""")
cursor.execute("""INSERT INTO Employee VALUES(1,'ZZZZZ',95000,'Admin');""")
cursor.execute("""INSERT INTO Employee VALUES(2,'XXXXX',45000,'IT');""")

connection.commit()

print("Table created successfuly")

cursor.execute("""SELECT * FROM Employee ORDER BY Eno DESC;""")
data = cursor.fetchall()
print(*data,sep="\n")

connection.close()
