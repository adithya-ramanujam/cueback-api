import mysql.connector
from random import randrange

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root_pwd2021",
    database = "reccomender_interface",
    auth_plugin='mysql_native_password'
    )

mycursor = mydb.cursor()

sql = "INSERT INTO recc_table (prompt_id, user_id, score) VALUES (%s, %s, %s)"

vals = []

for i in "ABCDE":
    for j in range(10):
        iD = i + str(j)
        score = randrange(10)
        sto = (iD, iD, score)
        vals.append(sto)

mycursor.executemany(sql, vals)

mydb.commit()

print(mycursor.rowcount, "was inserted")
    
