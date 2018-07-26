import pandas as pd
import matplotlib
import os

INPUT_FOLDER = "../preprocessing/aggregated/weekly/classes/"
OUTPUT_FOLDER = "../preprocessing/distributions/weekly/classes/"

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
		if colname == "GapSize" or colname == "BurstSize":
			continue
		graph_name = output_folder+colname+"-"+file_name.replace(".csv","")
		column = df[[colname]]
		colcount = column[colname]

		print("working on: " + colname)
		if colname in COLUMNS_TO_HISTOGRAM: 
			# create the logarithmic bins up to the max value
			maxval = colcount.max()
			bins = [-1,0,1]
			initial = 1
			while initial < maxval :
				initial *= 10
				bins.append(initial)

			# cut data into bins
			colcount = pd.cut(colcount, bins=bins).value_counts().sort_index()
			fig = colcount.plot.bar(rot=-45,logy=True).get_figure()
		else:
			colcount = colcount.value_counts().sort_index()
			fig = colcount.plot.bar().get_figure()

		fig.tight_layout()
		fig.savefig(graph_name)
		fig.clf()

		column = None
		fig = None
		colcount = None

def find_max_val_for_columns(file_path, cols):
	print("working on: " + file_path)
	data = pd.read_csv(file_path, sep=" ")
	df = pd.DataFrame(data)

	for colname in df.columns:
		column = df[[colname]]
		colcount = column[colname]

		if colname in cols:
			cols[colname] = max(cols[colname],colcount.max())
		else:
			cols[colname] = colcount.max()

def find_max_forall_in_folder(input_path):

	if not os.path.isdir(input_path):
		print("Error: path specified is not a folder.")
		return

	cols = {}

	for file_name in os.listdir(input_path):
		full_path = input_path+file_name
		if not os.path.isdir(full_path):
			find_max_val_for_columns(full_path, cols)

	for col in cols:
		print(col + " : " + str(cols[col]))

def draw_graphs_from_folder(input_path, output_folder):

	if not os.path.isdir(input_path):
		print("Error: path specified is not a folder.")
		return

	for file_name in os.listdir(input_path):
		full_path = input_path+file_name
		if not os.path.isdir(full_path):
			draw_graphs_for_columns(file_name, full_path, output_folder)


# draw_graphs_from_folder(INPUT_FOLDER, OUTPUT_FOLDER)
find_max_forall_in_folder(INPUT_FOLDER)
