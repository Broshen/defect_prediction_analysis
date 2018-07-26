import os
import subprocess
import sys
import re

INPUT_PATH = "../experiment_3/results/"

# takes in a path P.dot to a dot file representing a weighted directed graph, 
# and creates a undirected dot file and rendered jpg in the same
# directory called P_undirected.dot, P_undirected.jpg
def find_from_file(path):
	if not path.endswith("top_network.dot"):
	#	print("File " + path + " is not a .dot file")
		return

	parents = set()
	children = set()
	vertices = set()

	with open(path, "r+") as file:
		for line in file:
			if "->" in line:
				try:
					m = re.match(r'(.*)\[(.*)"\];', line)
					edge = m.group(1)
				except:
					edge = line.replace(";", "")

				parent, child = edge.split("->")
				parents.add(parent.strip())
				children.add(child.strip())

			if "->" not in line and "{" not in line and ";" in line: #vertex declaration
				vertices.add(line.replace(";","").strip())

	print(path)
	#print(parents)
	#print(children)
	for vertex in vertices:
#		print(vertex, vertex in parents, vertex in children)
		if not(vertex in parents and vertex in children):
			print(vertex)

def find_all_in_folder(directory):
	for path in os.listdir(directory):
		fullpath = directory+path

		if os.path.isdir(fullpath):
			find_all_in_folder(fullpath + "/")
		else:
			find_from_file(fullpath)

find_all_in_folder(INPUT_PATH)