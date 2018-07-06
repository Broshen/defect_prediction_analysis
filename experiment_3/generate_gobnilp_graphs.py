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

GOBNILP_EXECUTABLE_PATH = "../gobnilp.spx"
GOBNILP_SETTINGS_PATH = "./gobnilp.set"
INPUT_FILE_PATH = '../preprocessing/discretized/weekly/classes/'
OUTPUT_FILE_PATH = "./bn_graphs/weekly/classes/"

def generateDotFiles(file, output_folder):
	out_name=file.replace("_incl_bugs-gobnilp_formatted.csv", "")
	out_file=output_folder+out_name+"_bn.dot"

	subprocess.call([GOBNILP_EXECUTABLE_PATH, "-f=dat", "-g="+GOBNILP_SETTINGS_PATH, INPUT_FILE_PATH+file])

	with open(output_folder+out_name+"_scores", "w+") as scorefile:
		# iterate through results and move & rename to appropriate folder
		for file in os.listdir("./"):
			if file.startswith("bn") and file.endswith("dot"):
				subprocess.call(["mv",  file, output_folder+out_name+"_"+file])


def generateAllFiles():
	if not os.path.exists(OUTPUT_FILE_PATH):
		os.makedirs(OUTPUT_FILE_PATH)

	for file in os.listdir(INPUT_FILE_PATH):
		if "_incl_bugs-gobnilp_formatted.csv" in file:
			generateDotFiles(file, OUTPUT_FILE_PATH)

def generateFromFilesWithPrefix(prefix):
	if not os.path.exists(OUTPUT_FILE_PATH):
		os.makedirs(OUTPUT_FILE_PATH)

	for file in os.listdir(INPUT_FILE_PATH):
		if (INPUT_FILE_PATH + file).startswith(prefix):
			generateDotFiles(file, OUTPUT_FILE_PATH)

try:
	print("GENERATING FROM FILES BEGINNING WITH: " + sys.argv[1])
	generateFromFilesWithPrefix(sys.argv[1])
except:
	print("GENERATING FROM ALL FILES IN FOLDER" + INPUT_FILE_PATH)
	generateAllFiles()
