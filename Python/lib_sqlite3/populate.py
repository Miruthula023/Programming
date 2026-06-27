# populate means inserting record in a table usong insert into command
import sqlite3 

def fun():
	
	connection = sqlite3.connect("populate.db")
	cursur = connection.cursor()

	cmnd = """CREATE TABLE classA(rollno INTEGER , name CHAR(10),place CHAR(10));"""
	cursur.execute(cmnd)

	print("TABLE CREATED SUCCESFULLY")

	cmnd = """INSERT INTO classA VALUES(1,"XXXX","YYYY");"""
	cursur.execute(cmnd)

	print("VALUES ADDED SUCCESFULLY")
	connection.commit()
	connection.close()


fun()
