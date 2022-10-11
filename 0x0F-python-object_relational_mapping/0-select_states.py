#!/usr/bin/python3
"""
The script lists all states from the db using MySQLdb
"""
import MySQLdb

def mysqlconnect(mysql_username, mysql_password, database_name):
    """connects to the sqldb and executes queries"""

    db_connect = MySQLdb.connect("localhost@3306", mysql_username,\
                                 mysql_password, database_name)

    cursor = db_connect.cursor()

    cursor.execute("SELECT * FROM states.hbtn_0e_0_usa ORDER BY ASC states.id;")

    db_connect.close()


if "__main__" == "__name__":
    mysqlconnect()
