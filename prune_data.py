import pandas as pd
import os

INPUT_FOLDER = './preprocessing/discretized/weekly/classes/'
OUTPUT_FOLDER = './preprocessing/pruned_discretized/weekly/classes/'


COLUMNS_TO_KEEP = {
"ECLIPSE20_GAP3-3_BURST3-3":
	["NumberCodeBurstsLate","PeopleTotal","NumberOfDefects","TotalBurstSizeEarly","TLOC","MaxChurnInBurst","pre",],
"ECLIPSE20_ALLGAPS_ALLBURSTS":
	["NumberOfChangesLate","PeopleTotal","NumberOfDefects","GapSize","MaximumCodeBurstLate","TimeLastBurst","TimeFirstBurst","MaxChurnInBurst","pre","TLOC","MaximumCodeBurst","TotalPeopleInBurst",],
"ECLIPSE21_GAP3-3_BURST3-3":
	["TimeLastBurst","MaximumCodeBurstLate","PeopleTotal","NumberOfDefects","TotalPeopleInBurst","pre","MaxChurnInBurst",],
"ECLIPSE21_ALLGAPS_ALLBURSTS":
	["NumberOfChangesEarly","PeopleTotal","NumberOfDefects","pre","TotalPeopleInBurst","MaxChurnInBurst","TimeLastBurst","MaximumCodeBurstLate","TotalBurstSizeLate",],
"ECLIPSE30_GAP3-3_BURST3-3":
	["NumberOfChangesEarly","PeopleTotal","NumberOfDefects","TotalPeopleInBurst","MaximumCodeBurstLate","MaxChurnInBurst","TLOC","NumberOfChanges","pre",],
"ECLIPSE30_ALLGAPS_ALLBURSTS":
	["NumberConsecutiveChangesLate","PeopleTotal","NumberOfDefects","pre","GapSize","MaximumCodeBurstLate","TimeFirstBurst","TimeLastBurst","NumberCodeBursts","NumberOfChanges",],
"ECLIPSE31_GAP3-3_BURST3-3":
	["TimeLastBurst","PeopleTotal","bugs","MaxChurnInBurst","TotalBurstSizeEarly",],
"ECLIPSE31_ALLGAPS_ALLBURSTS":
	["NumberConsecutiveChangesLate","PeopleTotal","bugs","MaximumCodeBurstLate","TotalBurstSizeLate","MaxPeopleInBurst","TimeMaxBurst",],
}

# expects a .csv filename, whose file has ; seperators
def prune_from_burst_file(file_name, prefix_key, output_folder):
	print("formatting: " + file_name)
	data = pd.read_csv(file_name, sep=" ")
	df = pd.DataFrame(data)

	df = df[COLUMNS_TO_KEEP[prefix_key]]

	output_file_name = os.path.basename(file_name)
	
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	df.to_csv(path_or_buf=output_folder+output_file_name, sep=" ", index=False)

def prune_discretized_data(input_path, output_folder):

	if os.path.isdir(input_path):
		for file_name in os.listdir(input_path):

			subpath = input_path+file_name
			prune_discretized_data(subpath, output_folder)
	else:
		prefix_key = os.path.basename(input_path).replace("_incl_bugs-gobnilp_formatted.csv","")
		prune_from_burst_file(input_path, prefix_key, output_folder)
		


prune_discretized_data(INPUT_FOLDER, OUTPUT_FOLDER)
