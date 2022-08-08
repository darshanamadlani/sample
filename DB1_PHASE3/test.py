import MySQLdb
from MySQLdb import MySQLError
from flask_mysqldb import MySQL

try:
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "",
                           db = "doctoral")
    cursor = conn.cursor()
    # c.execute("SELECT * FROM tt")
    # data =  c.fetchall()
    # print("db working")
    # print(data)
except MySQLError as ex:
    print("not working")
