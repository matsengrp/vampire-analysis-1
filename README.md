# Analysis notebooks and scripts for the first paper about [vampire](https://github.com/matsengrp/vampire)

This repository makes the plots for the paper _Deep generative models for T cell receptor protein sequences_ by Kristian Davidsen, Branden J Olson, William S DeWitt III, Jean Feng, Elias Harkins, Philip Bradley and Frederick A Matsen IV.

To make the figures in the paper, download results files from <https://zenodo.org/record/2619576#.XKElTrfYphE> and place in an `input` directory in the root of this repository. Make an `output` directory as well.

Then run these notebooks in the `vampire` conda environment built as described in the main vampire repository.
You will also need to execute jupyter as follows:

    conda install jupyter
    conda install -c r r-irkernel

as well as install the R packages `cowplot`, `latex2exp`, and `reshape2`.


## Reproducing results

The results for this paper took quite considerable computing power, and require a compute cluster.
As described in the main vampire repository, you will need to modify the `execute.py` script to work for your cluster in order to do the computation.

### Comparative analyses

To build the results for plotting,

* download the relevant data from immuneACCESS
* run `python util.py split-repertoires` from the main repository (you can see an example call in `_output_deneuter-2019-02-07/deneuter-2019-02-07.json`)
* Run `scons --data=/path/to/the/resulting/json/file.json`

### Cohort frequency analysis

This repo also includes a script `prep-cohort-frequency.sh` that prepares files for the cohort frequency analysis.
If you want to reproduce this analysis,

* download [the data](https://clients.adaptivebiotech.com/pub/emerson-2017-natgen) from Adaptive
* preprocess it using `preprocess_adaptive.py` script in the vampire repository
* run the `prep-cohort-frequency.sh` script (editing paths)
* run the `pipe_freq` pipeline with `scons --pipe=pipe_freq` (editing the path in the SConstruct file)
