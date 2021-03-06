TODOLIST:
Week of July 26
- Investigate why burst/gap size appear to be independent from other variables in experiment 5.
- Further analysis on which variables seem to be closely related to NumberOfDefects. See if some are consistently connected to it, or if there is no pattern here.
- Look into letting GOBNILP run fully (i.e. overnight) on larger datasets (e.g. experiment 3), see how this would affect the structure of the resulting BNs.
- Building out a queryable program, based on the structure of some of the BNs, i.e. write a program that can calculate the probability function, and make predictions, given a dataset and a BN
	- Test and evaluate how accurate it is on our datasets, compared to traditional regression models, after building it out.
- Look into other ways of "pruning" the dataset, and what those BNs would  look like:
	- ONLY variables that are <= 2 degrees of seperation away from NumberOfDefects or pre
	- ONLY those in the the same "branch" as NumberOfDefects or pre
	- ONLY 1 variable per type - e.g. out of MaximumCodeBurst, MaximumCodeBurstEarly, MaximumCodeBurstLate, ONLY take MaximumCodeBurst, etc. (or whichever one seems to affect NumberOfDefects the most)
- Look into enforcing ancestor constraints - i.e. FORCE NumberOfDefects to be a leaf node, or force specific paths to exist in the BNs.
	- compare the GOBNILP scores between the best/optimal BNs and the ones where ancestor constraints are enforced

Week of July 6
- ~~combine 3-3 and ALL, see which edges appear in one or both~~
- ~~generate top 10, used "aggregated" graphs~~
- investigate into presolving for scores faster, try to get optimal scores (try BDM scoring?)
- ~~redo experiment_1, experiment_2 with properly discretized sets?~~

Week of June 10
- ~~investigate combining various datasets (e.g. all of the ECLIPSEX_BURSTX_GAPX) into a single dataset by adding additional variables that capture the differences~~
	- ~~add gap size and burst size as columns, and combine~~
		- ~~combine 1-3, 4-6, 7-10 for burst & gap size~~
		- ~~work with /weekly/classes data for now~~
		- ~~DONT combine datasets from different versions (e.g. ECLIPSE20 + ECLIPSE21), as this will double count many changes (duplicates)~~
- ~~add LOC (lines of code) as a column to datasets~~
- ~~proper discretization (instead of quartiling) all data columns:~~
	- ~~plot histograms/frequency distributions of all columns to consider~~
	- ~~consider common patterns:~~
		- ~~top 5%, middle 90%, bottom 5%~~
		- ~~zeros, top 5%, leftovers~~
		- ~~zero, one, > 1 ~~
- investigate removing columns that are correlated - e.g. NumberOfChanges vs NumberOfChangesLate vs NumberOfChangesEarly
	- look into using a correlation matrix to determine which to remove
- compare ECLIPSE dataset with other datasets
- folder structure documentation
- compare BN from optimal predictor dataset (gap size=3, burst size=3) with BN from general/aggregated dataset


Week of June 3rd
- ~~generate top 100 BNs for a specific dataset, aggregate that~~
	- ~~make sure all BNs have a similar score, otherwise discard~~ (experiment_2)
- ~~try to treat edges as undirected (for experiment_1 and experiment_2) see if that simplifies the aggregated structure~~

Week of May 27th, May 23rd
~~run & generate from different datasets, see if patterns persists in graphs~~ - experiment_1

investigate getting weights onto edges
investigate using conditional probability values as weights (instead of the ones generated by GOBNILP)
investigate ways to measure how similar graphs are, software to pick out patterns in multiple graphs
investigate using weka to preprocess and optimally discretize data
play around with variations on columns to include/exclude, classes vs packages
try GOBNILP with different scoring metrics (BIC vs BDM)
read up about conditional independence assumptions
