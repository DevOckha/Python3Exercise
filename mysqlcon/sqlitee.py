import sqlite3
from sqlite3.dbapi2 import connect


connection = sqlite3.connect("node_app.db")

cursor = connect.cursor()

connect.close()