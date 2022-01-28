import sqlite3
from os import path

conn = sqlite3.connect('../sql/sample.db')
c = conn.cursor()
# c.execute('SELECT email, last, first FROM users ORDER BY last')

# for row in c.fetchall():
# 	print(row[0], row[1], row[2])

# Using a parameter, last=? which looks for x
# x = 'Kirk','Chan',
# c.execute('SELECT email,last,first FROM users WHERE last=? OR last=?',x)
# for row in c.fetchall():
# 	print(row[0], row[1], row[2])

# Scalar values
# c.execute('SELECT count (email) FROM users')
# for row in c.fetchall():
# 	print(row[0])

# Insert with parameters
# x = 'john@mail.com', 'John', 'Doe',
# c.execute('INSERT INTO users VALUES (?,?,?)',x)

# for row in c.execute('SELECT * FROM users ORDER BY email'):
# 	print(row)

# Delete duplicates
c.execute('DELETE from users WHERE rowid NOT IN (SELECT min(rowid) FROM users GROUP BY last, first)');

for row in c.execute('SELECT * FROM users ORDER BY email'):
	print(row)

conn.commit()
conn.close()