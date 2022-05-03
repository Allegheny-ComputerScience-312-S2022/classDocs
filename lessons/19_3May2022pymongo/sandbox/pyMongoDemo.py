#!/usr/bin/env python3

# Date 3 May 2022
# pymongo demo for python3



# Note: Leave this code inside your MongoDB Docker container so that it can access the database.

from pymongo import MongoClient
import string


def read():
	""" function to read records from mongo db """
	try:
		empCol = db.Employee.find()
		print("\n Found: all data from DataEmployee \n")
		for emp in empCol:
			print(f"\t [+] {emp}")
	except Exception as e:
		print(str(e))
# end of read()



def insert():
	""" Function to insert data into mongo db """
	try:
		employeeId = input('Enter Employee id :')
		employeeFirstName = input('Enter FirstName :')
		employeeLastName = input('Enter LastName :')
		employeeAge = input('Enter age :')
		employeeCountry = input('Enter Country :')

	# insert the data into the base
		db.Employee.insert_one(
		{
		"id": employeeId,
		"firstName":employeeFirstName,
		"lastName":employeeLastName,
		"age":employeeAge,
		"country":employeeCountry
		})
		print("\nInserted data successfully\n")

	except Exception as e:
		print(str(e))
# end of insert()



def update():
	""" Function to update record to mongo db """
	print("  Update:")
	try:

		employeeId = input('  Enter Employee id :')
		employeeFirstName = input('  Enter FirstName :')
		employeeLastName = input('  Enter LastName :')
		employeeAge = input('  Enter age :')
		employeeCountry = input('  Enter Country :')


	# update the record with the new information
		db.Employee.update_one(
		{"id": employeeId},
		{
		"$set": {
		"firstName":employeeFirstName,
		"lastName":employeeLastName,
		"age":employeeAge,
		"country":employeeCountry
		}
		})
		print("\nRecords updated successfully. \n")
	except Exception as e:
		print(str(e))
# end of update()



# creating connections for communicating with MongoDB
client = MongoClient('localhost:27017')
db = client.mongodemo # The name of the collection is mongodemo

# read the collection
print("\t [+] Data BEFORE addition")
read()

# populate the collection
print("\t [+] Insert some data")
insert()

# read the collection
print("\t [+] Data AFTER addition")
read()

# Update data in the collection; all fields have to be entered again
print("\t [+] Update Data")
update()

# read the collection
print("\t [+] Data AFTER Update")
read()
