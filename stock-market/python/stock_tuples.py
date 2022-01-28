import csv


stock_list = []

	
stocks = ['aapl', 'f']

for stock in stocks: 
	file = open("../datasets/" + stock + ".csv", "r")
	reader = csv.reader(file)
	headers = next(reader, None)

	for x in reader:
		# date, open, close, volume
		stock_date_close_open = (x[9], x[0], x[5])
		stock_list.append(stock_date_close_open)

	file.close()

print(len(stock_list))