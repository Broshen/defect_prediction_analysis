## File Descriptions

To run any python script, simply run `python scriptname.py` in this directory

aggregate_data.py - aggregates multiple datasets (from the change_burst_data repo), with different BURST and GAP sizes, into one large dataset, under `../preprocessing/aggregated/` 

direct_dot_to_undirected.py - converts a directed graph into an undirected graph, and draws out the result using graphviz. To run, call `python direct_dot_to_undirected.py PATH/TO/DIRECTED/GRAPH.dot`. The resulting undirected graph and image will be saved in the same folder as the directed graph specified.

find_roots_and_leaves.py - given a folder, will find all the .dot graph files within that folder and all of it's subfolders, and outputs the nodes that are roots (i.e. only have edges going outwards) or leaves (only have edges going inwards) for each file.
Used to find the nodes to keep for experiment_4, based on the results of experiment_3

format_data.py - takes all the datasets found in ../preprocessing/aggregated, and creates a discretized dataset for each file, saved to ../preprocessing/discretized, where each column is binned according to their distribution, specified in the script.

plot_columns.py - takes all the datasets found in ../preprocessing/aggregated, and draws plots for the frequencies of each column in each file, saving it to ../preprocessing/distributions. Used to examine and determine how to categorize each variable (see proposed_discretization_segments.txt)

prune_data.py - takes all the datasets found in ../preprocessing/discretized, and for each dataset, drops all columns not specified by a variable for that specific dataset, defined in the script, saving the resulting dataset to ../preprocessing/pruned_discretized. Used to create the datasets for experiment_4, based on the roots and leaves found in experiment_3

simplify_data.py - takes all the datasets found in ../preprocessing/discretized, and for each dataset, drop all columns not specified by a common variable for all datasets, saving the resulting dataset to ../preprocessing/simplified_discretized. Used to create the datasets for experiment_5
