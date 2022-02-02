import csv
from sqlite3 import DateFromTicks
import pygal
from pygal.style import CleanStyle


stock_prices = {}
stock_sym = ['aapl', 'f']

for symbol in stock_sym:
	file_name = "../datasets/" + symbol + ".csv"
	f = open(file_name, "r")
	reader = csv.reader(f)
	next(reader, None)
	dates = []
	dataset = []
	count = 0
	# date[9], close[0]
	for x in reader:
		count = count + 1
		if count%10 ==0:
			dates.append(x[9])
			dataset.append(float(x[0]))
	stock_prices[symbol] = list(reversed(dataset))

line_chart = pygal.Line(style=CleanStyle)
line_chart.title = "Stock Prices"
line_chart.x_labels = dates 
for symbol in stock_sym:
	line_chart.add(symbol, stock_prices[symbol])

line_chart.render_to_file('stocks-chart.svg')