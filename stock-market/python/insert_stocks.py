import csv
import sqlite3


stock_list = []

stocks = ['aapl', 'f']

for stock in stocks: 
	file = open("../datasets/" + stock + ".csv", "r")
	reader = csv.reader(file)
	headers = next(reader, None)

	for x in reader:
		# date[9], close[0], high[1], low[2], 
		# open[3], volume[5], symbol[4]
		tup = (x[9], x[0], x[1], x[2], x[3], x[5], x[4])
		stock_list.append(tup)

	file.close()

# Add to db

conn = sqlite3.connect('../sql/stocks.db')
c = conn.cursor()

c.executemany('INSERT INTO stockprices VALUES (?, ?, ?, ?, ?, ?, ?)',stock_list)
conn.commit()
conn.close()

print(c.rowcount)