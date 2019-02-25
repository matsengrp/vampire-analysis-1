set -eux

# python build_sparse.py --out-path output/hansen666.matrix.pkl $(find /fh/fast/matsen_e/matsen/hansen-666-preprocessed/ -name "*.csv")
# python scripts/select_subjects.py
#python scripts/sample_data_set.py --n-to-sample 200000 output/hansen666.subject_subsampled.csv.train.csv.bz2 output/all-subjects.train.200K.csv
tcr-vae train output/basic_params.json output/all-subjects.train.200K.csv output/all-subjects.train.200K.best_weights.h5 output/diagnostics.csv
head -n 10000 output/all-subjects.train.200K.csv > output/all-subjects.train.200K.head.csv
tcr-vae pvae output/basic_params.json output/all-subjects.train.200K.best_weights.h5 output/all-subjects.train.200K.head.csv output/all-subjects.train.200K.head.pvae.csv
