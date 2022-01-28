import csv


stock_list = []
stock_dict = {}
	
stocks = ['aapl', 'f']

for stock in stocks: 
	file = open("../datasets/" + stock + ".csv", "r")
	reader = csv.reader(file)
	headers = next(reader, None)

	for x in reader:
		# close[0], open[3], volume[5], date[9]
		stock_date_close_open = (x[9], x[0], x[5])
		stock_list.append(stock_date_close_open)

		tuple_key = (stock, x[9])
		stock_dict[tuple_key] = x[0]

	file.close()

print(len(stock_list))	# prints 506

print(stock_dict[('aapl', '2021-06-01')]) # prints 124.28