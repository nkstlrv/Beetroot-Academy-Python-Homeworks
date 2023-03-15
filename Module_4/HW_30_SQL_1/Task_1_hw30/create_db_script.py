import sqlite3

connection = sqlite3.connect('hw30_task1_sqlite_db')

cursor = connection.cursor()

cursor.execute("CREATE TABLE test_tb (a int, b int);")

cursor.execute("DROP TABLE test_tb;")

connection.commit()
connection.close()