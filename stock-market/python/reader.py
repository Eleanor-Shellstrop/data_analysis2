import csv


stocks = ['aapl', 'f', 'msft']

for stock in stocks: 
	file = open("../datasets/" + stock + ".csv", "r")
	reader = csv.reader(file)
	headers = next(reader, None)

	print(headers)

	count = 0

	for x in reader:
		# date, open, close, volume
		print(x[0], x[1], x[4], x[5])
		count = count + 1

	print(count)

	file.close()