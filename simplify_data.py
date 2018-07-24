import pandas as pd
import os

INPUT_FOLDER = './preprocessing/discretized/weekly/classes/'
OUTPUT_FOLDER = './preprocessing/simplified_discretized/weekly/classes/'


COLUMNS_TO_KEEP = ["PeopleTotal", "NumberOfChanges", "ChurnTotal"]
COLUMNS_TO_KEEP_20_21_30 = ["TLOC", "pre", "NumberOfDefects"]
COLUMNS_TO_KEEP_31 = ["bugs"]
COLUMNS_TO_KEEP_MERGED = ["BurstSize", "GapSize"]

# expects a .csv filename, whose file has ; seperators
def simpify(file_name, output_folder):
	print("formatting: " + file_name)
	data = pd.read_csv(file_name, sep=" ")
	df = pd.DataFrame(data)

	columns = COLUMNS_TO_KEEP

	if "ECLIPSE31" in file_name:
		columns = columns + COLUMNS_TO_KEEP_31
	else:
		columns = columns + COLUMNS_TO_KEEP_20_21_30

	if "ALLGAPS_ALLBURSTS" in file_name:
		columns = columns + COLUMNS_TO_KEEP_MERGED

	df = df[columns]

	output_file_name = os.path.basename(file_name)
	
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	df.to_csv(path_or_buf=output_folder+output_file_name, sep=" ", index=False)

def simplify_dir(input_path, output_folder):

	if os.path.isdir(input_path):
		for file_name in os.listdir(input_path):
			subpath = input_path+file_name
			simplify_dir(subpath, output_folder)
	else:
		simpify(input_path, output_folder)
		


simplify_dir(INPUT_FOLDER, OUTPUT_FOLDER)
