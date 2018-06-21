import pandas as pd
import matplotlib
import os

INPUT_FOLDER = "./preprocessing/aggregated/weekly/classes/"
OUTPUT_FOLDER = "./preprocessing/distributions/weekly/classes/"

COLUMNS_TO_HISTOGRAM = {
	"MaxChurnInBurst",
	"TotalChurnInBurst",
	"ChurnTotal",
	"TLOC"
}

# expects a .csv filename, whose file has ; seperators
def draw_graphs_for_columns(file_name, file_path, output_folder):
	print("working on: " + file_path)
	data = pd.read_csv(file_path, sep=" ")
	df = pd.DataFrame(data)

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
	
	for colname in df.columns:
		print("working on: " + colname)
		if colname == "GapSize" or colname == "BurstSize":
			continue

		graph_name = output_folder+colname+"-"+file_name.replace(".csv","")
		column = df[[colname]]
		colcount = column[colname].value_counts().sort_index()
		if colname in COLUMNS_TO_HISTOGRAM: 
			colcount.plot.hist(bins=5, logy=True).get_figure().savefig(graph_name)
		else:
			colcount.plot.bar().get_figure().savefig(graph_name)
		colcount.plot.bar().get_figure().clf()
		column = None
		colcount = None

def draw_graphs_from_folder(input_path, output_folder):

	if not os.path.isdir(input_path):
		print("Error: path specified is not a folder.")
		return

	for file_name in os.listdir(input_path):
		full_path = input_path+file_name
		draw_graphs_for_columns(file_name, full_path, output_folder)


draw_graphs_from_folder(INPUT_FOLDER, OUTPUT_FOLDER)
