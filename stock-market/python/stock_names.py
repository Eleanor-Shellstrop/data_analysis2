import csv


file = "../datasets/nyse.csv"

def get_stock_dict():
	stock_dict = {}

	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for data in reader:
			stock_dict[data[0]] = data[1]
	return stock_dict

stocks = get_stock_dict()

my_stocks = ['IBM', 'F', 'DIS']

for x in my_stocks:
	if x in stocks:
		print(stocks[x])