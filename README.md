## `split-repertoires` calls

### `adaptive-robins-ratio`

```
python util.py split-repertoires --limit-each 20000 --test-regex Healthy --out-prefix /fh/fast/matsen_e/matsen/vampire-analysis-1/data/adaptive-robins-ratio-2019-02-16 /fh/fast/matsen_e/data/adaptive-robins-ratio/MS_subject_*_CD4.tsv /fh/fast/matsen_e/data/adaptive-robins-ratio/Healthy_Subject_*_CD4_Naive.tsv

scons --data=/fh/fast/matsen_e/matsen/vampire-analysis-1/data/adaptive-robins-ratio-2019-02-16.json -j 75 --clusters=beagle
```


### `seshadri-six`
This is just a small sample split with 4 training repertoires and 2 test repertoires:

```
python util.py split-repertoires --limit-each 10000 --out-prefix /fh/fast/matsen_e/matsen/vampire-analysis-1/data/seshadri-six-2019-02-16 $(ls /fh/fast/matsen_e/data/seshadri/data/Adaptive/clinical_cohort/*TCRB* | head -n 6)
```

I then manually went and added
```
    "train_size": 20000
```
to the JSON file.


Run with

```
scons --mode=mini --data=/fh/fast/matsen_e/matsen/vampire-analysis-1/data/seshadri-six-2019-02-16.json -j 25 --clusters=koshu
```
