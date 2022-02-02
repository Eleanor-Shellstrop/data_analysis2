import csv
from sqlite3 import DateFromTicks
import pygal
from pygal.style import CleanStyle


stock_sym = ['googl']

for symbol in stock_sym:
	file_name = "../datasets/" + symbol + ".csv"
	f = open(file_name, "r")
	reader = csv.reader(f)
	next(reader, None)
	dates = []
	dataset = []
	# date[9], close[0]
	for x in reader:
		dates.append(x[9])
		dataset.append(float(x[0]))

line_chart = pygal.Line(style=CleanStyle)
line_chart.title = "Stock Prices"
line_chart.x_labels = dates 
line_chart.add("googl", dataset)

line_chart.render_to_file('stock-chart.svg')