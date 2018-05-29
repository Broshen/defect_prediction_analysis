import pandas as pd
import os

INPUT_FILE_PATH = '../change_burst_data-master/weekly/packages/'

# expects a .csv filename, whose file has ; seperators
def format_from_burst_file(file_name):
	print("formatting: " + file_name)
	data = pd.read_csv(file_name, sep=";")
	df = pd.DataFrame(data)

	# drop filename for now
	# TODO: bucketize filename by prefix
	df = df.drop(['filename'], axis=1)

	# drop metadata columns, keep only columns related to bursts
	# wrap in a try catch block as some files (ECLIPSE31_*) don't
	# have pre/NumberOfDefects columns, and has bugs column instead
	try:
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
	except KeyError:
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
		'bugs'
		]]

	# discretize all columns to maximum 4 categories
	for i in df:
		col = df[i]
		unique = len(col.unique())

		if unique > 4:
		 	df[i] = pd.cut(col,bins=4, labels=False)

	output_folder = os.path.dirname(file_name)+"/gobnilp_formatted/"
	output_file_name = os.path.basename(file_name).replace('.csv', "-gobnilp_formatted.csv")
	
	if not os.path.exists(output_folder):
		os.mkdir(output_folder)

	df.to_csv(path_or_buf=output_folder+output_file_name, sep=" ", index=False)

def format_change_burst_data(input_path):

	# standardize trailing slash
	if(input_path[-1] != "/"):
		input_path+="/"

	if os.path.isdir(input_path):
		for file_name in os.listdir(input_path):

			subpath = input_path+file_name

			# since the formatted folders may also be in the folder
			# we are iterating over, we don't want to reformat
			# the already formatted files
			if "/gobnilp_formatted/" not in subpath:
				if os.path.isdir(subpath):
					format_change_burst_data(subpath)
				else:
					format_from_burst_file(subpath)
	else:
		format_from_burst_file(input_path)
		


format_change_burst_data(INPUT_FILE_PATH)
