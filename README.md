# Defect Prediction Analysis:

Investigating the relationships between various metrics and defects in software projects by using Bayesian Networks

## Setup:
Prerequisites: 
python, pip, and virtualenv

1. set up and activate your python virtualenv in a folder. suppose this folder is called `/PROJECT`
2. create your project folder under `/PROJECT` - this will hold all of your datasets, programs, experiments, and results. suppose this folder is called `/ROOT`
3. under `/PROJECT/ROOT`, download and install:
a. GOBNILP: https://www.cs.york.ac.uk/aig/sw/gobnilp/ 
b. SCIP (for GOBNILP): http://scip.zib.de/
c. GraphViz: http://graphviz.org
d. The change burst dataset: https://github.com/kimherzig/change_burst_data
e. This repo: https://github.com/Broshen/defect_prediction_analysis
Instructions for installing GOBNILP, SCIP, and GraphViz are all on their respective sites.
4. At this point, your folder structure should look something like this:
```
\PROJECT
    \ROOT
        \change_burst_data-master
        \gobnilp163
        \graphviz-2.38
        \scipoptsuite-3.2.1
        \defect_prediction_analysis-master <- this repo
            \experiment_1
            \experiment_2
            ... etc ...
```
5. In \PROJECT\ROOT\defect_prediction_analysis-master, run pip install -r requirements.txt to install the necessary packages

## Files and folders

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

/preprocessing - preprocessed datasets - these are the change_burst_data-master datasets that have been merged, discretized, pruned, etc., that are actually used in the experiments

/scripts - helper scripts to preprocess datasets, and analyze generated BNs

/sample_* - an example of what you might try to feed into GOBNILP, what may come out, and the resulting graph & structure

/Experiment_Analysis_Summary.pdf - detailed writeup of the experiments done so far

/writeup.docx - draft of the writeup

/TODOLIST.md - a list of future experiments/things to investigate (as well as past things that have already been done)

/requirements.txt - python packages required for some of the scripts


## Running Experiments Manually 
To compute an optimal network, install GOBNILP, and run `./PATH_TO_GOBNILP_EXECUTABLE -f=dat -g=gobnilp.set ./PATH_TO_DATA_FILE.dat` from this directory - e.g. `bin/gobnilp -f=dat -g=gobnilp.set sample_gobnilp_input.dat`

To see a graph drawn from a GOBNILP output:
	Install graphviz (http://graphviz.org)
	Ensure that your gobnilp settings file has the setting `gobnilp/outputfile/dot = SOME_FILE_NAME.dot` set
	Compute the network as usual (as specified above). There should be a SOME_FILE_NAME.dot file outputted afterwards
	Run `./PATH/TO/GRAPHVIZ/EXECUTABLES/dot.exe -Tjpg PATH/TO/SOME_FILE_NAME.dot -o OUTPUT_IMAGE_NAME.jpg`
	