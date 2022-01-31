import csv
from datetime import datetime
from dateutil.parser import parse


# Goal: Calculate value of holdings over time
# Goal: Calc and sort daily diff of holdings over time

# Key is tuple (symbol, date)
# Value is tuple (open, close)
stock_dict = {}

stock_sym = "googl"
file_name = "../datasets/" + stock_sym + ".csv"

f = open(file_name, "r")
reader = csv.reader(f)
next(reader, None) # Skip headers

# date[9], open[3], high[1], low[2], close[0], volume[5]
for data in reader:
	stock_dict[(stock_sym, parse(data[9]))] = float(data[3]), float(data[0])

for x in stock_dict:
	print(x, stock_dict[x])
print(len(stock_dict))