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
stock_list = get_stocks()

# Write pickle- serialized data
pickled_stocks = open("pickled_stocks.dat", "wb")

pickle.dump(stock_list, pickled_stocks, 4)
pickled_stocks.close()