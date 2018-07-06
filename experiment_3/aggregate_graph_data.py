import os
import subprocess
import sys
from collections import OrderedDict
from operator import itemgetter  

GRAPHVIZ_DOT_EXECUTABLE_PATH="../../graphviz-2.38/release/bin/dot.exe"
GRAPH_FOLDER_PATH = sys.argv[1]
OUTTPUT_FOLDER_PATH = sys.argv[2]

def draw_graphs(input_folder, output_folder):

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	for file in os.listdir(input_folder):

		if file.endswith("dot"):
			subprocess.call([GRAPHVIZ_DOT_EXECUTABLE_PATH, "-Tjpg", input_folder+file, "-o",output_folder+file.replace(".dot",".jpg")])

draw_graphs(GRAPH_FOLDER_PATH, OUTTPUT_FOLDER_PATH)
