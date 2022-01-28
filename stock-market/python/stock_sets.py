watchlist = ['MSFT', 'AAPL', 'QCOM']
openpos = [('AAPL', 100.00, 100), ('F', 8.35, 100), ('DIS', 87.35, 100)] #sym, buy, share
closedpos = [('MSFT', 25.50, 32.65, 100), ('INTC', 35.35, 27.89, 100)] #sym, buy, sell, share

my_stocks = set()

for x in watchlist:
	my_stocks.add(x)

for x in openpos:
	my_stocks.add(x[0])

for x in closedpos:
	my_stocks.add(x[0])

print(my_stocks)