import os
import subprocess
import sys
import re
from collections import OrderedDict
from operator import itemgetter  

GRAPHVIZ_DOT_EXECUTABLE_PATH="../../graphviz-2.38/release/bin/dot.exe"
DIRECTORY = "./results/"

legendTemplate = """
  rankdir=LR
  node [shape=plaintext]
  subgraph cluster_01 {{ 
    label = "Legend";
    key [label=<<table border="0" cellpadding="2" cellspacing="0" cellborder="0">
      <tr><td align="right" port="i1">{0}</td></tr>
      <tr><td align="right" port="i2">{1}</td></tr>
      <tr><td align="right" port="i3">{2}</td></tr>
      </table>>]
    key2 [label=<<table border="0" cellpadding="2" cellspacing="0" cellborder="0">
      <tr><td port="i1">&nbsp;</td></tr>
      <tr><td port="i2">&nbsp;</td></tr>
      <tr><td port="i3">&nbsp;</td></tr>
      </table>>]
    key:i1:e -> key2:i1:w [color=red]
    key:i2:e -> key2:i2:w [color=blue]
    key:i3:e -> key2:i3:w [color=black]
  }}
"""

def compare(file1, file2, output_file_path, output_image_path, use_weights):
	edge_map = {}
	name1 = file1.split("/")[-1]
	name2 = file2.split("/")[-1]

	with open(file1, 'r') as myfile:
		for line in myfile:
			if " -> " in line:
				try:
					m = re.match(r'(.*)\[label="(.*)",weight="(.*)"\];', line)
					edge = m.group(1) + ";"
					weight = int(m.group(2))
				except:
					edge = line
					weight = 1
				edge = edge.strip()

				if edge in edge_map:
					edge_map[edge]+= weight if use_weights else 1
				else:
					edge_map[edge]= weight if use_weights else 1

	with open(file2, 'r') as myfile:
		for line in myfile:
			if " -> " in line:
				try:
					m = re.match(r'(.*)\[label="(.*)",weight="(.*)"\];', line)
					edge = m.group(1) + ";"
					weight = int(m.group(2))
				except:
					edge = line
					weight = 1
				edge = edge.strip()

				if edge in edge_map:
					edge_map[edge]-= weight if use_weights else 1
				else:
					edge_map[edge]= -weight if use_weights else -1

	# sort dictionary and print values
	with open(output_file_path, "w+") as networkfile:
		networkfile.write("digraph {\n")
		for item in OrderedDict(sorted(edge_map.items(), key = itemgetter(1), reverse = True)):

			if edge_map[item] == 0:
				color = "black"
			elif edge_map[item] > 0:
				color = "red"
			else:
				color = "blue"

			if use_weights:
				networkfile.write(item.strip().replace(";", "[label=\""+str(edge_map[item])+"\",weight=\""+str(edge_map[item])+"\", color=\""+color+ "\"];\n"))
			else:
				networkfile.write(item.strip().replace(";", "[color=\""+color+ "\"];\n"))

		if use_weights:
			networkfile.write(legendTemplate.format(
				"Appears more frequently in " + name1,
				"Appears more frequently in " + name2,
				"Appears in both graphs"
			))
		else:
			networkfile.write(legendTemplate.format(
				"Appears in " + name1,
				"Appears in " + name2,
				"Appears in both graphs"
			))

		networkfile.write("}")

	subprocess.call([GRAPHVIZ_DOT_EXECUTABLE_PATH,
		"-Tjpg",
		output_file_path,
		"-o", output_image_path])

def compare_aggregated(input_folder):
	candidate_files = []
	# first find candidate files
	for path in os.listdir(input_folder):
		fullpath = input_folder+path
		if not os.path.isdir(fullpath) and path.endswith("_aggregate_network.dot"):
			candidate_files.append(fullpath)

	if len(candidate_files) > 2:
		print("WARNING: more than 2 aggregated_network.dot files found:") 
		print(candidate_files)
		print("Only first 2 will be used")

	if len(candidate_files) < 2:
		print("ERROR: less than 2 aggregated_network.dot files found. Exiting")
		return

	compare(candidate_files[0], candidate_files[1],
		input_folder+"aggregated_networks_comparison.dot",
		input_folder+"aggregated_networks_comparison.jpg",
		True)


def compare_top(input_folder):
	candidate_files = []
	# first find candidate files
	for path in os.listdir(input_folder):
		fullpath = input_folder+path
		if not os.path.isdir(fullpath) and path.endswith("_top_network.dot"):
			candidate_files.append(fullpath)

	if len(candidate_files) > 2:
		print("WARNING: more than 2 top_network.dot files found:") 
		print(candidate_files)
		print("Only first 2 will be used")

	if len(candidate_files) < 2:
		print("ERROR: less than 2 top_network.dot files found. Exiting")
		return

	compare(candidate_files[0], candidate_files[1],
		input_folder+"top_network_comparison.dot",
		input_folder+"top_network_comparison.jpg",
		False)

def compare_top_vs_aggregated(input_folder, file_prefix):
	candidate_files = []

	for path in os.listdir(input_folder):
		fullpath = input_folder+path
		if not os.path.isdir(fullpath) and path.endswith("network.dot") and path.startswith(file_prefix):
			candidate_files.append(fullpath)

	if len(candidate_files) > 2:
		print("WARNING: more than 2 .dot files starting with " + file_prefix + "found:") 
		print(candidate_files)
		print("Only first 2 will be used")

	if len(candidate_files) < 2:
		print("ERROR: less than 2 .dot files starting with " + file_prefix + "found. Exiting")
		return

	compare(candidate_files[0], candidate_files[1],
		input_folder+ file_prefix + "_top_vs_aggregated.dot",
		input_folder+ file_prefix + "_top_vs_aggregated.jpg",
		False)


for path in os.listdir(DIRECTORY):
	fullpath = DIRECTORY+path
	if os.path.isdir(fullpath):
		fullpath += "/"
		compare_top(fullpath)
		compare_aggregated(fullpath)
		compare_top_vs_aggregated(fullpath, "ALLGAPS_ALLBURSTS")
		compare_top_vs_aggregated(fullpath, "GAP3-3_BURST3-3")
	else:
		print(path + " is not a directory, skipping")