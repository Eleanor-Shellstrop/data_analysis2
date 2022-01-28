import sqlite3
from os import path

conn = sqlite3.connect('../sql/sample.db')
c = conn.cursor()
c.execute('SELECT email FROM users')

for row in c.fetchall():
	print(row[0])