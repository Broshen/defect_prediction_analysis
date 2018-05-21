import pandas as pd
import os

INPUT_FILE_PATH = '../change_burst_data-master/weekly/packages/Eclipse20_GAP1_BURST1_incl_bugs.csv'
OUTPUT_FILE_PATH = '../change_burst_data-master/formatted/'

def format_change_burst_data(input_path, is_folder, output_folder, file_name):
	if is_folder:
		print("NOT IMPLEMENTED YET")
		# TODO: format all of the files in folder and subdirectory
	else:
		data = pd.read_csv(input_path, sep=";")
		df = pd.DataFrame(data)

		# drop filename for now
		# TODO: bucketize filename by prefix
		df = df.drop(['filename'], axis=1)

		# drop metadata columns, keep only columns related to bursts
		df = df[[
		'TotalPeopleInBurst',
		'MaximumCodeBurstLate',
		'NumberOfChanges',
		'MaxPeopleInBurst',
		'TotalBurstSizeLate',
		'NumberCodeBurstsLate',
		'NumberOfChangesLate',
		'NumberOfChangesEarly',
		'MaxChurnInBurst',
		'MaximumCodeBurstEarly',
		'NumberCodeBurstsEarly',
		'TimeFirstBurst',
		'TotalChurnInBurst',
		'ChurnTotal',
		'MaximumCodeBurst',
		'NumberOfConsecutiveChangesEarly',
		'NumberConsecutiveChangesLate',
		'TotalBurstSizeEarly',
		'TotalBurstSize',
		'TimeMaxBurst',
		'NumberConsecutiveChanges',
		'TimeLastBurst',
		'NumberCodeBursts',
		'PeopleTotal',
		'pre',
		'NumberOfDefects'
		]]
		# discretize all columns to maximum 10 categories
		for i in df:
			col = df[i]
			unique = len(col.unique())

			if unique > 4:
			 	df[i] = pd.cut(col,bins=4, labels=False)

		if not os.path.exists(output_folder):
			os.mkdir(output_folder)
		df.to_csv(path_or_buf=output_folder+file_name, sep=" ", index=False)


format_change_burst_data(INPUT_FILE_PATH, False, OUTPUT_FILE_PATH, 'test.dat')

		#
