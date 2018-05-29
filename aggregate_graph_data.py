import os

GRAPH_FOLDER_PATH="./bn_graphs/"
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
		elif "_BN.dot" in fullpath:
			aggregate_file(fullpath)
		else:
			print("Invalid file name - must contain _BN.dot: " + fullpath)

aggregate(GRAPH_FOLDER_PATH)

# sort dictionary and print values

from collections import OrderedDict
from operator import itemgetter  

for item in OrderedDict(sorted(EDGE_MAP.items(), key = itemgetter(1), reverse = True)):
	print(item.strip(), EDGE_MAP[item])