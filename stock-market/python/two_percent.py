import csv


count = 0
two_percent = []
file = '../datasets/stock_data.csv'

with open(file, 'r') as csvfile:

	reader = csv.reader(csvfile)

	for row in reader:
		name = row[0]
		opn = float(row[2])
		cls = float(row[3])
		chg = (cls - opn) / opn
		if chg > 0.02:
			print(name + " " + str(chg))
			count = count + 1

print(count)