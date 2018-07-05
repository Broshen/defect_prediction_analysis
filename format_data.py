import pandas as pd
import os

INPUT_FOLDER = './preprocessing/aggregated/weekly/classes/'
OUTPUT_FOLDER = './preprocessing/discretized/weekly/classes/'

BINS = {
	'bugs': [-1,0,10],
	'ChurnTotal': [-1,0,10,100,1000,100000],
	'MaxChurnInBurst': [-1, 0, 10, 100, 1000,100000],
	'MaximumCodeBurst': [-1,0, 100],
	'MaximumCodeBurstEarly': [-1,0, 100],
	'MaximumCodeBurstLate': [-1,0, 100],
	'MaxPeopleInBurst': [-1, 0, 100],
	'NumberCodeBursts': [-1, 0, 100],
	'NumberCodeBurstsEarly': [-1,0, 100],
	'NumberCodeBurstsLate': [-1, 0, 10],
	'NumberConsecutiveChanges': [-1,0,1,10, 100],
	'NumberConsecutiveChangesLate': [-1,0,1,10, 100],
	'NumberOfChanges': [-1,0,1,2, 100],
	'NumberOfChangesEarly': [-1,0,1,2, 100],
	'NumberOfChangesLate': [-1,0,1,2, 100],
	'NumberOfConsecutiveChangesEarly': [-1,0,1,10, 100],
	'NumberOfDefects': [-1, 100],
	'PeopleTotal': [-1, 0, 100],
	'pre': [-1, 0, 100],
	'TLOC': [-1, 10, 100, 10000],
	'TotalBurstSize': [-1, 0, 100],
	'TotalBurstSizeEarly': [-1, 0, 100],
	'TotalBurstSizeLate': [-1, 0, 100],
	'TotalChurnInBurst': [-1, 0, 10, 100, 1000, 100000],
	'TotalPeopleInBurst': [-1, 0, 100],

	# NOT included:

	# 'TimeFirstBurst': 0-1, rest in equal thirds
	# 'TimeLastBurst': 0-1, rest in equal thirds
	# 'TimeMaxBurst': 0-1, rest in equal thirds
	# GapSize, BurstSize: leave as 10 discrete values
}

# expects a .csv filename, whose file has ; seperators
def format_from_burst_file(file_name, output_folder):
	print("formatting: " + file_name)
	data = pd.read_csv(file_name, sep=" ")
	df = pd.DataFrame(data)

	# discretize all columns to maximum 4 categories
	for colname in df:
		print(colname)
		column = df[colname]

		if colname == "GapSize" or colname == "BurstSize":
			continue
		elif (colname == "TimeFirstBurst" or
			colname == "TimeLastBurst" or
			colname == "TimeMaxBurst"):
		# do -1, rest in thirds
			bins=[-2,0,]
			maxval = column.max()
			b1 = int(maxval/3)
			b2 = 2*b1
			bins.append(b1)
			bins.append(b2)
			bins.append(maxval+1)

			df[colname] = pd.cut(column,bins=bins, labels=False)
		elif colname in BINS:
			df[colname] = pd.cut(column,bins=BINS[colname], labels=False)
		else:
			print("ERROR: BINS FOR " + colname + "NOT DEFINED")


	output_file_name = os.path.basename(file_name).replace('.csv', "-gobnilp_formatted.csv")
	
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	df.to_csv(path_or_buf=output_folder+output_file_name, sep=" ", index=False)

def format_change_burst_data(input_path, output_folder):

	if os.path.isdir(input_path):
		for file_name in os.listdir(input_path):

			subpath = input_path+file_name
			format_change_burst_data(subpath, output_folder)
	else:
		format_from_burst_file(input_path, output_folder)
		


format_change_burst_data(INPUT_FOLDER, OUTPUT_FOLDER)
