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
# c.execute('DELETE from users WHERE rowid NOT IN (SELECT min(rowid) FROM users GROUP BY last, first)');
# for row in c.execute('SELECT * FROM users ORDER BY email'):
# 	print(row)


# Insert another record, show count
# x = 'jane@mail.com', 'Jane', 'Doe',
# c.execute('INSERT INTO users VALUES (?,?,?)',x)


# Update entries
# x = 'Johnny','john@mail.com'
# c.execute('UPDATE users SET first=? WHERE email=?',x)


# Delete entry
# x = 'john@mail.com',
# c.execute('DELETE FROM users WHERE email=?',x)


# Insert many records
employees = [('jill@mail.com', 'Jill', 'Appletree'),
			('frank@mail.com', 'Frank', 'Appletree'), 
			('desi@mail.com', 'Desi', 'Appletree'),]
c.executemany('INSERT INTO users values (?,?,?)', employees)
for row in c.execute('SELECT * FROM users ORDER BY email'):
 	print(row)

conn.commit()
conn.close()

print(c.rowcount)