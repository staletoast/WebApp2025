import sqlite3 as sql

def listExtension():
    con = sql.connect(".database/database.db")
    cur = con.cursor()
  data = cur.execute('SELECT * FROM extension').fetchall()
    con.close()
    return data