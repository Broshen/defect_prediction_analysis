# IMPORTANT: READ ME
# This python script is run on the student.linux environments,
# since it runs the gobnilp executables, which was set up there
# (it's a pain in the ass to set up on windows)
# The student linux environments only have Python 2.7
# Hence, this script is in Python 2.7!!!!
# (whereas other scripts are all in python 3)
# !!!!!THIS PYTHON SCRIPT IS WRITTEN IN PYTHON 2.7!!!!!

import os
import subprocess
import sys

GOBNILP_EXECUTABLE_PATH = "./gobnilp.spx"
GOBNILP_SETTINGS_PATH = "./gobnilp.set"
INPUT_FILE_PATH = '../change_burst_data-master/weekly/packages/gobnilp_formatted/'
OUTPUT_FOLDER = "./gobnilp_networks/"

def generateDotFiles(file, output_folder):
	out_name=file.replace("_incl_bugs-gobnilp_formatted.csv", "")
	subprocess.call([GOBNILP_EXECUTABLE_PATH, "-f=dat", "-g="+GOBNILP_SETTINGS_PATH, INPUT_FILE_PATH+file])

	# iterate through results and move & rename to appropriate folder
	for bnfile in os.listdir("./"):
		if bnfile.startswith("bn") and bnfile.endswith("dot"):
			subprocess.call(["mv",  bnfile, output_folder+out_name+"_"+bnfile])


def generateAllFiles():
	output_folder=INPUT_FILE_PATH.replace("../change_burst_data-master", "./bn_graphs").replace('gobnilp_formatted/', '')

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	for file in os.listdir(INPUT_FILE_PATH):
		if "_incl_bugs-gobnilp_formatted.csv" in file:
			generateDotFiles(file, output_folder)

def generateFromFilesWithPrefix(prefix):
	output_folder=INPUT_FILE_PATH.replace("../change_burst_data-master", "./bn_graphs").replace('gobnilp_formatted/', '')

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	for file in os.listdir(INPUT_FILE_PATH):
		if (INPUT_FILE_PATH + file).startswith(prefix):
			generateDotFiles(file, output_folder)

try:
	print("GENERATING FROM FILES BEGINNING WITH: " + sys.argv[1])
	generateFromFilesWithPrefix(sys.argv[1])
except:
	print("GENERATING FROM ALL FILES IN FOLDER" + INPUT_FILE_PATH)
	generateAllFiles()

# stopped at ../change_burst_data-master/weekly/packages/gobnilp_formatted/Eclipse20_GAP1_BURST10_incl_bugs-gobnilp_formatted.csv