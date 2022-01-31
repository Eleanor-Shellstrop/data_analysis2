import csv
from datetime import datetime
from dateutil.parser import parse
import operator


shares = {"googl": 10, "f": 1000}
market_dates = []
# Key is tuple (symbol, date)
# Value is tuple (open, close)
myDict = {}

for x in shares.keys():
	stock_sym = x
	file_name = "../datasets/" + stock_sym + ".csv"

	f = open(file_name, "r")
	reader = csv.reader(f)
	next(reader, None) # Skip headers

	# date[9], open[3], high[1], low[2], close[0], volume[5]
	for data in reader:
		if parse(data[9]) not in market_dates:
			market_dates.append(parse(data[9]))
		myDict[(stock_sym, parse(data[9]))] = float(data[3]), float(data[0])

# print(myDict)

diff = {}

# TODO: Won't work, find fix
# for date in sorted(market_dates):
# 	for stk in shares.keys():
# 		if date in total:
# 			total[date] = total[date] + myDict[(stk, date)][1]*shares[stk]
# 		else:
# 			total[date] = myDict[(stk, date)][1]*shares[stk]

# for date in sorted(market_dates):
# 	print(date, total[date])


# for date in sorted(market_dates):
# 	for stk in shares.keys():
# 		if date in diff:
# 			close_less_open = (myDict[(stk, date)][1] - myDict[(stk, date)][0])
# 			diff[date] = diff[date] + close_less_open * shares[stk]
# 		else:
# 			diff[date] = (myDict[(stk, date)][1] - myDict[(stk, date)][0]) * shares[stk]

# for date in sorted(market_dates):
# 	print(date, diff[date])