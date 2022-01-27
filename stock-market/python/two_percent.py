import os
import csv


script_dir = os.path.dirname(__file__)
file = "..\datasets\stock_data.csv"
full_path = os.path.join(script_dir, file)

count = 0
two_percent = []

with open(full_path, 'r') as csvfile:

	reader = csv.reader(csvfile)

	for row in reader:
		name = row[0]
		date = row[1]
		opn = float(row[2])
		cls = float(row[3])
		chg = (cls - opn) / opn
		if chg > 0.02:
			two_percent.append(date + " " + name + " " + str(chg))
			count = count + 1

two_percent.sort()
print(two_percent)