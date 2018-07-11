import os
import subprocess
import sys
import re
from collections import OrderedDict
from operator import itemgetter  

GRAPHVIZ_DOT_EXECUTABLE_PATH="../../graphviz-2.38/release/bin/dot.exe"

GRAPH_FOLDER_PATH =  "./bn_graphs/weekly/classes/"
OUTPUT_FOLDER_PATH = "./results/"

EDGE_THRESHOLD = 0.5

def aggregate_folder(folder, dataset_version, dataset_name):
	total_files = 0
	edge_map = {}
	output_folder = OUTPUT_FOLDER_PATH+dataset_version+"/"

	# create the output folder
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	# aggregate all the edges
	for file in os.listdir(folder):
		fullpath = folder+file
		print(folder)
		total_files += 1

		if fullpath.endswith("bn_1.dot"):
			subprocess.call(["cp", fullpath, output_folder+dataset_name+"_top_network.dot"])
			subprocess.call([GRAPHVIZ_DOT_EXECUTABLE_PATH, "-Tjpg", fullpath, "-o",output_folder+dataset_name+"_top_network.jpg"])

		with open(fullpath, 'r') as myfile:
			for line in myfile:
				# super simple way to detect whether a line represents an edge declaration
				# for now, instead of having to install graphviz and parse the entire
				# dot file
				if " -> " in line:
					if line in edge_map:
						edge_map[line]+=1
					else:
						edge_map[line]=1

	# sort dictionary and print values
	with open(output_folder+dataset_name+"_aggregate_network.dot", "w+") as networkfile, open(output_folder+dataset_name+"_common_edges.txt", "w+") as commonedges:

		networkfile.write("digraph {\n")
		commonedges.write("Format:\nEdge; Number of graphs this edge appears in\n")

		for item in OrderedDict(sorted(edge_map.items(), key = itemgetter(1), reverse = True)):
			# only include the edge in the aggregated graph if it meets the threshold
			if edge_map[item] >= EDGE_THRESHOLD * total_files:
				networkfile.write(item.strip().replace(";", "[label=\""+str(edge_map[item])+"\",weight=\""+str(edge_map[item])+"\"];\n"))

			commonedges.write(item.strip() + " " + str(edge_map[item])+"\n")

		networkfile.write("}")

	subprocess.call([GRAPHVIZ_DOT_EXECUTABLE_PATH,
		"-Tjpg",
		output_folder+dataset_name+"_aggregate_network.dot",
		"-o", output_folder+dataset_name+"_aggregate_network.jpg"])

def aggregate(directory):
	for path in os.listdir(directory):
		fullpath = directory+path

		if os.path.isdir(fullpath):
			fullpath+="/"
			try:
				m = re.match(r'(.*)_(.*)_(.*)', path)
				dataset_version = m.group(1)
				dataset_name = m.group(2) + "_" + m.group(3)
			except:
			 	print("ERROR: " + path + " DOES NOT MEET THE REQUIRED FORMAT: ECLIPSE(version)_(GAPSIZE)_(BURSTSIZE)")
			aggregate_folder(fullpath, dataset_version, dataset_name)
		else:
			print("WARNING: " + fullpath + " IS NOT A FOLDER")
	
aggregate(GRAPH_FOLDER_PATH)
