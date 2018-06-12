import os
import subprocess
import sys
from collections import OrderedDict
from operator import itemgetter  

GRAPHVIZ_DOT_EXECUTABLE_PATH="../../graphviz-2.38/release/bin/dot.exe"
EDGE_MAP = {}


def aggregate_file(file):
	with open(file, 'r') as myfile:
		for line in myfile:
			# super simple way to detect whether a line represents an edge declaration
			# for now, instead of having to install graphviz and parse the entire
			# dot file
			if " -> " in line:
				if line in EDGE_MAP:
					EDGE_MAP[line]+=1
				else:
					EDGE_MAP[line]=1

def aggregate(directory):
	for path in os.listdir(directory):
		fullpath = directory+path

		if os.path.isdir(fullpath):
			if fullpath[-1] != "/":
				fullpath+="/"
			aggregate(fullpath)
		elif ".dot" in fullpath:
			aggregate_file(fullpath)

def output_result(output_folder):

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	# sort dictionary and print values
	with open(output_folder+"aggregate_network.dot", "w+") as networkfile, open(output_folder+"common_edges.txt", "w+") as commonedges:

		networkfile.write("digraph {\n")
		commonedges.write("Format:\nEdge; Number of graphs this edge appears in\n")

		for item in OrderedDict(sorted(EDGE_MAP.items(), key = itemgetter(1), reverse = True)):
			networkfile.write(item.strip().replace(";", "[label=\""+str(EDGE_MAP[item])+"\",weight=\""+str(EDGE_MAP[item])+"\"];\n"))
			commonedges.write(item.strip() + " " + str(EDGE_MAP[item])+"\n")


		networkfile.write("}")

	subprocess.call([GRAPHVIZ_DOT_EXECUTABLE_PATH, "-Tjpg", output_folder+"aggregate_network.dot", "-o",output_folder+"aggregate_network.jpg"])

GRAPH_FOLDER_PATH = sys.argv[1]
OUTTPUT_FOLDER_PATH = sys.argv[2]

aggregate(GRAPH_FOLDER_PATH)
output_result(OUTTPUT_FOLDER_PATH)
