import sqlite3
import pickle


def get_stocks():
	stock_list = []
	conn = sqlite3.connect('../sql/stocks.db')
	c = conn.cursor()
	c.execute('SELECT date, close, high, low, open, volume, symbol FROM stockprices')
	for row in c.fetchall():
		stock_tuple = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
		stock_list.append(stock_tuple)
		return stock_list

# Initial List
stock_list = []
stock_list = [get_stocks]
print(len(stock_list))

# Write pickle- serialized data
pickle_stocks = open("pickle_stocks.dat", "wb")
# Protocol 0 (ascii), 1 (binary), or 2 (binary)
pickle.dump(stock_list, pickle_stocks, 2)
pickle_stocks.close()