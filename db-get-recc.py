import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root_pwd2021",
    database = "reccomender_interface",
    auth_plugin='mysql_native_password'
    )

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM recc_table")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
