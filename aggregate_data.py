import pandas as pd
import os
import re

INPUT_FOLDER = '../change_burst_data-master/weekly/classes/'
OUTPUT_FOLDER = "./preprocessing/aggregated/weekly/classes/"


columns_to_keep = [
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
		'TLOC',
		'pre',
		'NumberOfDefects',
		'bugs'
		]


def aggregate_by_version_gap_burst(folder, output_folder, version, gap_min, gap_max, burst_min, burst_max):
	print("Aggregating all csv files in {0} with version {1}, gap size {2}-{3}, burst size {4}-{5}".format(
		folder, version, gap_min, gap_max, burst_min, burst_max))

	df = None

	if not os.path.isdir(folder):
		print("Error: path specified is not a folder.")
		return

	for file_name in os.listdir(folder):
		filereg = re.match(r'^Eclipse(.*)_GAP(.*)_BURST(.*)_incl_bugs\.csv$', file_name)
		if not bool(filereg):
			print("skipping " + file_name + ": incorrect file name")
			return

		file_version = filereg.group(1)
		gapsize = filereg.group(2)
		burstsize = filereg.group(3)

		if file_version != version:
			print("Skipping {0} - version {1} does not match {2} specified".format(file_name, file_version, version))
			continue

		if int(gapsize) > gap_max or int(gapsize) < gap_min:
			print("Skipping {0} - gapsize {1} not in range of {2} - {3}".format(file_name, gapsize, gap_min, gap_max))
			continue

		if int(burstsize) > burst_max or int(burstsize) < burst_min:
			print("Skipping {0} - burstsize {1} not in range of {2} - {3}".format(file_name, burstsize, burst_min, burst_max))
			continue

		print("Working on file: " + file_name)
		fullpath = folder + file_name
		data = pd.read_csv(fullpath, sep=";")
		file_df = pd.DataFrame(data)

		# drop metadata columns
		for colname in file_df.columns:
			if colname not in columns_to_keep:
				file_df = file_df.drop([colname], axis=1)

		# add in column for burst size and gap size
		file_df['GapSize'] = gapsize
		file_df['BurstSize'] = burstsize

		if df is None:
			df = file_df
		else:
			df= pd.concat([df, file_df])

	output_file_name = output_folder + "ECLIPSE{0}_GAP{1}-{2}_BURST{3}-{4}_incl_bugs.csv".format(version,gap_min,gap_max,burst_min,burst_max)
	print("Writing " + output_file_name + " to disk")

	if not os.path.isdir(output_folder):
		os.makedirs(output_folder)

	df.to_csv(path_or_buf=output_file_name, sep=" ", index=False)

# expects a folder with .csv files
def aggregate_by_version(folder, output_folder, version):
	print("Aggregating all csv files in {0} with version  {1}".format(folder, version))

	df = None

	if not os.path.isdir(folder):
		print("Error: path specified is not a folder.")
		return

	for file_name in os.listdir(folder):
		filereg = re.match(r'^Eclipse(.*)_GAP(.*)_BURST(.*)_incl_bugs\.csv$', file_name)
		if not bool(filereg):
			print("skipping " + file_name + ": incorrect file name")
			return

		file_version = filereg.group(1)
		gapsize = filereg.group(2)
		burstsize = filereg.group(3)

		if file_version != version:
			print("Skipping " + file_name +
				" - version " + file_version + " does not match " + version + " specified")
			continue

		print("Working on file: " + file_name)
		fullpath = folder + file_name
		data = pd.read_csv(fullpath, sep=";")
		file_df = pd.DataFrame(data)

		# drop metadata columns
		for colname in file_df.columns:
			if colname not in columns_to_keep:
				file_df = file_df.drop([colname], axis=1)

		# add in column for burst size and gap size
		file_df['GapSize'] = gapsize
		file_df['BurstSize'] = burstsize

		if df is None:
			df = file_df
		else:
			df= pd.concat([df, file_df])

	output_file_name = output_folder + "ECLIPSE" + version + "_ALLGAPS_ALLBURSTS_incl_bugs.csv"
	print("Writing " + output_file_name + " to disk")

	if not os.path.isdir(output_folder):
		os.makedirs(output_folder)

	df.to_csv(path_or_buf=output_file_name, sep=" ", index=False)


def aggregate_by_version_gap(folder, output_folder, version):
	aggregate_by_version_gap_burst(folder, output_folder, version, 1,3,1,10)
	aggregate_by_version_gap_burst(folder, output_folder, version, 4,6,1,10)
	aggregate_by_version_gap_burst(folder, output_folder, version, 7,10,1,10)

def aggregate_by_version_burst(folder, output_folder, version):
	aggregate_by_version_gap_burst(folder, output_folder, version, 1,10,1,3)
	aggregate_by_version_gap_burst(folder, output_folder, version, 1,10,4,6)
	aggregate_by_version_gap_burst(folder, output_folder, version, 1,10,7,10)


def aggregate_cartesian_product(folder, output_folder, version):
	sizes = [[1,3],[4,6],[7,10]]

	for size1 in sizes:
		for size2 in sizes:
			aggregate_by_version_gap_burst(folder, output_folder, version, size1[0], size1[1], size2[0], size2[1])



# aggregate_by_version_gap(INPUT_FOLDER, OUTPUT_FOLDER, "20")
# aggregate_by_version_gap(INPUT_FOLDER, OUTPUT_FOLDER, "21")
# aggregate_by_version_gap(INPUT_FOLDER, OUTPUT_FOLDER, "30")
# aggregate_by_version_gap(INPUT_FOLDER, OUTPUT_FOLDER, "31")
# aggregate_by_version_burst(INPUT_FOLDER, OUTPUT_FOLDER, "20")
# aggregate_by_version_burst(INPUT_FOLDER, OUTPUT_FOLDER, "21")
# aggregate_by_version_burst(INPUT_FOLDER, OUTPUT_FOLDER, "30")
# aggregate_by_version_burst(INPUT_FOLDER, OUTPUT_FOLDER, "31")
# aggregate_cartesian_product(INPUT_FOLDER, OUTPUT_FOLDER, "20")
# aggregate_cartesian_product(INPUT_FOLDER, OUTPUT_FOLDER, "21")
# aggregate_cartesian_product(INPUT_FOLDER, OUTPUT_FOLDER, "30")
# aggregate_cartesian_product(INPUT_FOLDER, OUTPUT_FOLDER, "31")
aggregate_by_version(INPUT_FOLDER, OUTPUT_FOLDER, "20")
aggregate_by_version(INPUT_FOLDER, OUTPUT_FOLDER, "21")
aggregate_by_version(INPUT_FOLDER, OUTPUT_FOLDER, "30")
aggregate_by_version(INPUT_FOLDER, OUTPUT_FOLDER, "31")
aggregate_by_version_gap_burst(INPUT_FOLDER, OUTPUT_FOLDER, "20", 3,3,3,3)
aggregate_by_version_gap_burst(INPUT_FOLDER, OUTPUT_FOLDER, "21", 3,3,3,3)
aggregate_by_version_gap_burst(INPUT_FOLDER, OUTPUT_FOLDER, "30", 3,3,3,3)
aggregate_by_version_gap_burst(INPUT_FOLDER, OUTPUT_FOLDER, "31", 3,3,3,3)