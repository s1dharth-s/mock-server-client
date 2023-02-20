# Populates a mock db with random data

import sqlite3
from os import path


def create_database():
    if not path.exists("sql_app.db"):
        con = sqlite3.connect("sql_app.db")

        datas = [('Luke Skywalker','Tatooine'), ('Harry Potter','Hogwarts'), ('Homer Simpson','Springfield')]

        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS payloads (id INTEGER PRIMARY KEY, name TEXT, city TEXT)')
        cur.executemany("INSERT INTO PAYLOADS (name, city) VALUES (?, ?)", datas) 

        con.commit()
        con.close()
    else:
        print("Database already exists!")