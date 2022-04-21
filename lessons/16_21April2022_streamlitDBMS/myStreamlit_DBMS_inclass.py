# cs312s2022

# import libraries
import streamlit as st
import pandas as pd
import sqlite3

myDBFile_str = "myCampusDB.sqlite3"
conn = sqlite3.connect(myDBFile_str)
c = conn.cursor()

def sql_executor(myCommand_str):
	"""the function to interact with db and provide it with commands"""
	c.execute(myCommand_str)
	data = c.fetchall()
	return data
	# end sql_executor()

def main():
	""" main driver function for the program"""
	st.title("My Streamlit DBMS") # establish a title for the app

	menu_list = ["Home", "About", "Start the WEEKEND!"]
	choice = st.sidebar.selectbox("Menu",menu_list)

	if choice == "Home":
		st.subheader("Database output")

	# layout screen using cols and rows
	myCol1, myCol2 = st.columns(2)

	with myCol1:
		st.write("Hello, this is myCol1")
		with st.form(key='query_form'):
			myCommand_str = st.text_area("Sql code goes here")
			submit_button = st.form_submit_button("Execute")

			st.write("command to list tables")
			tmp_str = "SELECT name FROM sqlite_master WHERE type = 'table';"

			st.code(tmp_str, language = 'bash')

		if submit_button:
			#st.balloons()
			#st.snow()
			st.info("Query has been submitted")
			st.code(myCommand_str)


			# make a results area
			query_results = sql_executor(myCommand_str)

# end of main()


if __name__ == '__main__':
	main()
