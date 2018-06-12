Defect Prediction Analysis:

Investigating the relationships between various metrics and defects in software projects.

To compute an optimal network, install GOBNILP, and run `./PATH_TO_GOBNILP_EXECUTABLE -f=dat -g=gobnilp.set ./PATH_TO_DATA_FILE.dat` from this directory - e.g. `bin/gobnilp -f=dat -g=gobnilp.set sample_gobnilp_input.dat`

To see a graph drawn from a GOBNILP output:
	Install graphviz (http://graphviz.org)
	Ensure that your gobnilp settings file has the setting `gobnilp/outputfile/dot = SOME_FILE_NAME.dot` set
	Compute the network as usual (as specified above). There should be a SOME_FILE_NAME.dot file outputted afterwards
	Run `./PATH/TO/GRAPHVIZ/EXECUTABLES/dot.exe -Tjpg PATH/TO/SOME_FILE_NAME.dot -o OUTPUT_IMAGE_NAME.jpg`
	

Folders:
/experiment_1 - generate the top 10 BNs from multiple eclipse datasets (e.g. EclipseX_GAPX_BURST_X), and try to aggregate them to find similarities/patterns between them by counting how many times an edge appears in all of the BNs.
/experiment_2 - generate the top 100 BNs from a single dataset, and try to aggregate them to find similarities/patterns between them
	- ensure that all suboptimal BNs have a similar score, otherwise, data may be skewed/inaccurate