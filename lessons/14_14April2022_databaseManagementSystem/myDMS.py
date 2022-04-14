#!/usr/bin/env python3

# 14 April 2022

# load libraries
import sqlite3

def buildTable(in_str, conn):
	""" Function to build my table. In_str is the table create command as a string and conn is the connection to the db."""

	print(f"\t [+] buildTable()::\n\t {in_str}")
	try:
		print(f"\t [+] Trying to build new table: {in_str}")
		conn.execute(in_str) # execute the creation command
		conn.commit() # save the changes
	except sqlite3.OperationalError:
		print(f"\t [-] Error exception handled.")
		print(f"\t [-] Table already exists.")

	# end of buildTable()

def addData(in_str, conn):
	""" execute insert statements. in_str is an insert statement, conn is connection to db."""

	print(f"\t [+] This is a the addData() function.")
	print(f"\n\tInsert statement:\n\t {in_str}")

	conn.execute(in_str) # send command to the DB to add data
	conn.commit() # save the changes.

	#end addData()

def executeQuery(in_str,conn):
	""" function to execute the query string. in_str is the query as a string and conn is the connection to the database"""

	# Send query to DB
	myResult = conn.execute(in_str) # run the query
	print(f" [+] Results from query: {myResult}")

	# Get result from query
	queryInfo_list = myResult.fetchall()
	print(f" [+] Fetchall results from query: {queryInfo_list}")

	for i in queryInfo_list:
		print(f"\t[+] {i}")

	# end of executeQuery()

def main():
	""" Driver function of program"""
	print("\t [+] This is a the main() function.")

#########################
# connect to the database
	dbFile_str = "myDB.sqlite3" # name of the current database
	conn = sqlite3.connect(dbFile_str) # open a connection to the base

	# Def of database: musical archive

#########################
# Create the table
# SQL Code: CREATE TABLE StudyMusic (id INTEGER NOT NULL, favSong VARCHAR, bandname VARCHAR )

	myTable_str = "StudyMusic"
	attribute1_str = "id INTEGER NOT NULL"
	attribute2_str = "favSong VARCHAR"
	attribute3_str = "bandname VARCHAR"

	myBuildTable = f"CREATE TABLE {myTable_str} ({attribute1_str}, {attribute2_str}, {attribute3_str})"

	# make a function to build the table:: buildTable()
	buildTable(myBuildTable, conn) # add the insert command to database


#########################
# add data to the table
# SQL Code: INSERT INTO StudyMusic VALUES (id INTEGER NOT NULL, favSong VARCHAR, bandname VARCHAR )

	myTable_str = "StudyMusic"
	attribute1_str = "1"
	attribute2_str = "\"Database Rock\""
	attribute3_str = "\"Oliver and the Bonham-Carterians\""

	myInsert_str = f"INSERT INTO {myTable_str} VALUES ({attribute1_str}, {attribute2_str}, {attribute3_str} )"

	addData(myInsert_str, conn)

# add more data
	myTable_str = "StudyMusic"
	attribute1_str = "2"
	attribute2_str = "\"Let data live\""
	attribute3_str = "\"Oliver and the Bonham-Carterians\""

	myInsert_str = f"INSERT INTO {myTable_str} VALUES ({attribute1_str}, {attribute2_str}, {attribute3_str} )"

	addData(myInsert_str, conn)

#########################
# Queryt data in a table
# SQL Code: SELECT id, favsong, bandname FROM StudyMusic;

# define table attributes
	myTable_str = "StudyMusic"
	attribute1_str = "id"
	attribute2_str = "favSong"
	attribute3_str = "bandname"

	myQuery_str = f"SELECT {attribute1_str}, {attribute2_str}, {attribute3_str} FROM {myTable_str}"

	print(f" [+] Running Query:\n {myQuery_str}")
	executeQuery(myQuery_str, conn) #run the query
	conn.close() # close the database connection

	#end of main()
main() # call the main driver of the program
