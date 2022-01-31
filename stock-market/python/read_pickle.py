import pickle
import stockpickle


objdump = None

with open('pickled_stocks.dat', 'rb') as f:
	objdump = pickle.load(f)
	for x in objdump:
		print(x[0], x[1], x[6])