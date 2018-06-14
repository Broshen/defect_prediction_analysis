import os
import subprocess
import sys
import re
from collections import OrderedDict
from operator import itemgetter  

GRAPHVIZ_DOT_EXECUTABLE_PATH="../graphviz-2.38/release/bin/dot.exe"
EDGE_MAP = {}

# takes in a path P.dot to a dot file representing a weighted directed graph, 
# and creates a undirected dot file and rendered jpg in the same
# directory called P_undirected.dot, P_undirected.jpg
def convert_weighted_digraph_to_graph(path):
	if not path.endswith(".dot"):
		print("File must be a .dot file")
		return

	with open(path, "r+") as digraphfile:
		firstline = digraphfile.readline()
		while not firstline:
			firstline = digraphfile.readline()

		if "digraph" not in firstline:
			print("File must be a valid digraph format")
			return

		for line in digraphfile:
			if "->" in line:
				m = re.match(r'(.*) -> (.*)\[label="(.*)",weight="(.*)"\];', line)
				node1 = m.group(1)
				node2 = m.group(2)
				weight = int(m.group(3))

				key = min(node1, node2) + " -- " + max(node1, node2) + ";"

				if key in EDGE_MAP:
					EDGE_MAP[key] += weight
				else:
					EDGE_MAP[key] = weight

	output_dot_path = path.replace('.dot', "_undirected.dot")
	output_jpg_path = path.replace('.dot', "_undirected.jpg")

	with open(output_dot_path, "w+") as outputdotfile:

		outputdotfile.write("graph {\n")

		for item in OrderedDict(sorted(EDGE_MAP.items(), key = itemgetter(1), reverse = True)):
			outputdotfile.write(item.strip().replace(";", "[label=\""+str(EDGE_MAP[item])+"\",weight=\""+str(EDGE_MAP[item])+"\"];\n"))

		outputdotfile.write("}")

	subprocess.call([GRAPHVIZ_DOT_EXECUTABLE_PATH, "-Tjpg", output_dot_path, "-o", output_jpg_path])

DIGRAPH_PATH = sys.argv[1]

convert_weighted_digraph_to_graph(DIGRAPH_PATH)