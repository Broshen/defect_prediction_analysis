import pandas as pd
import os

INPUT_FOLDER = './preprocessing/discretized/weekly/classes/'
OUTPUT_FOLDER = './preprocessing/pruned_discretized/weekly/classes/'


COLUMNS_TO_KEEP = {
"ECLIPSE20_ALLGAPS_ALLBURSTS":	
["NumberCodeBursts", "TLOC", "NumberOfDefects", "NumberOfChanges", "MaxChurnInBurst", "BurstSize", "TotalBurstSizeLate", "pre", "TimeFirstBurst", "NumberConsecutiveChanges", "MaximumCodeBurstLate", ]

,"ECLIPSE20_GAP3-3_BURST3-3":
["NumberCodeBursts", "NumberOfDefects", "NumberOfChanges", "MaximumCodeBurstEarly", "TotalPeopleInBurst", "NumberCodeBurstsEarly", "MaxChurnInBurst", "pre", "MaximumCodeBurstLate", "PeopleTotal", ]
	
,"ECLIPSE21_ALLGAPS_ALLBURSTS":
["MaximumCodeBurst", "NumberOfDefects", "NumberOfChangesEarly", "BurstSize", "TotalBurstSizeLate", "TimeLastBurst", "TimeFirstBurst", "MaximumCodeBurstLate", "PeopleTotal", ]

,"ECLIPSE21_GAP3-3_BURST3-3":
["NumberOfChangesLate", "MaximumCodeBurst", "NumberOfDefects", "MaxChurnInBurst", "TimeMaxBurst", "MaximumCodeBurstLate", "PeopleTotal", ]

,"ECLIPSE30_ALLGAPS_ALLBURSTS":
["NumberOfDefects", "NumberOfChanges", "TotalBurstSizeEarly", "TotalBurstSizeLate", "TimeLastBurst", "TimeFirstBurst", "TotalChurnInBurst", "MaximumCodeBurstLate", "PeopleTotal", ]

,"ECLIPSE30_GAP3-3_BURST3-3":
["NumberOfDefects", "NumberOfChanges", "TotalPeopleInBurst", "TotalBurstSizeEarly", "MaxChurnInBurst", "NumberConsecutiveChanges", "MaximumCodeBurstLate", "PeopleTotal", ]

,"ECLIPSE31_ALLGAPS_ALLBURSTS":
["bugs", "MaximumCodeBurst", "NumberOfChanges", "MaxChurnInBurst", "BurstSize", "TimeMaxBurst", "NumberConsecutiveChanges", "MaximumCodeBurstLate", "PeopleTotal", ]

,"ECLIPSE31_GAP3-3_BURST3-3":
["bugs", "NumberOfChanges", "MaximumCodeBurstEarly", "MaxChurnInBurst", "TimeMaxBurst", ]
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
