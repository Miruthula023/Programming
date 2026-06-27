import csv

with open("getstrt.csv") as csvfile:

	reader = csv.reader(csvfile,delimiter = ',')
	for row in csvfile:
		print(row)
