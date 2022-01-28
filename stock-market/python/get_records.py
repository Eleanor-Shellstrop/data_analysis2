import sqlite3
from os import path

conn = sqlite3.connect('../sql/sample.db')
c = conn.cursor()
# c.execute('SELECT email, last, first FROM users ORDER BY last')

# for row in c.fetchall():
# 	print(row[0], row[1], row[2])

# Using a parameter, last=? which looks for x
x = 'Kirk','Chan',
c.execute('SELECT email,last,first FROM users WHERE last=? OR last=?',x)
for row in c.fetchall():
	print(row[0], row[1], row[2])

conn.commit()
conn.close()