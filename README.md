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

/experiment_3 - generate the top 10 BNs from the MERGED dataset and the OPTIMAL dataset for each version
	1) compare the aggregated BNs between the MERGED and OPTIMAL datasets
	2) compare the best BNs (i.e. bn_1.dot) between the MERGED and OPTIMAL datasets
	3) compare the best BNs vs the aggregated BNs for each dataset

/experiment_4 - generate the top 10 BNs taking only the variables that are ONLY dependent, or ONLY independent, based on the best BN generated in experiment_3 for each dataset, and pruning all other variables
	1) compare the aggregated BNs between the MERGED and OPTIMAL datasets
	2) compare the best BNs (i.e. bn_1.dot) between the MERGED and OPTIMAL datasets
	3) compare the best BNs vs the aggregated BNs for each dataset

/experiment_5 - generate the top 10 BNs taking only the variables: {"TLOC", "BurstSize", "GapSize", "pre", "PeopleTotal", "NumberOfChanges", "NumberOfDefects", "ChurnTotal"}. The goal of this is to that many variables are counting the same, or similar things (e.g. NumberOfChanges, NumberOfChangesEarly, NumberOfChangesLate, etc.), so by only taking one of these variables, we can try to simplify the dataset, and try to observe more concrete patterns that may appear throughout multiple datasets. In addition to generating the top 10 BNs, we also:
	1) compare the aggregated BNs between the MERGED and OPTIMAL datasets
	2) compare the best BNs (i.e. bn_1.dot) between the MERGED and OPTIMAL datasets
	3) compare the best BNs vs the aggregated BNs for each dataset
