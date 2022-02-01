import csv
from datetime import datetime
from dateutil.parser import parse
import pandas as pd


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


# Make list for df
all_stocks = []

for stk, date in myDict:
	sym = stk
	day = date
	opn = myDict[(stk, date)][0]
	cls = myDict[(stk, date)][1]
	if sym == 'googl':
		opn = opn * 10
		cls = cls * 10
	if sym == 'f': 
		opn = opn * 1000
		cls = cls * 1000
	all_stocks.append([sym, day, opn, cls])

# DF for date and sum of stocks
df = pd.DataFrame(all_stocks)
df.columns = ["stock", "date", "opening_amt", "closing_amt"]

# DF for only day end totals
day_end_totals = df.groupby(["date"], as_index=False).agg({"closing_amt": "sum"})

# DF for day opening and day end totals
day_diff_totals = df.groupby(["date"], as_index=False).agg({"opening_amt": "sum", "closing_amt": "sum"})

# Add column for day difference
day_diff_totals["close_less_open"] = day_diff_totals["closing_amt"] - day_diff_totals["opening_amt"]
print(day_diff_totals.head(20))