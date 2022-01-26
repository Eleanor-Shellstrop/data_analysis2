import csv


with open('stock_data.csv', 'w', encoding='utf-8') as f:
	
	stocks = ['aapl', 'f']

	for stock in stocks: 
		file = open("../datasets/" + stock + ".csv", "r")
		reader = csv.reader(file)
		headers = next(reader, None)

		count = 0

		for x in reader:
			# date, open, close, volume
			# commas for csv
			f.write(stock + "," + x[9] + "," + x[3] + "," + x[0] + "," + x[5] + "\n")
			count = count + 1

		print(count)

		file.close()

f.close()
print("Done")