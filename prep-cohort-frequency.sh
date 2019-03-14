set -eux

python scripts/sparse_count_df.py --out-path output/hansen666.matrix.pkl $(find /fh/fast/matsen_e/matsen/hansen-666-preprocessed/ -name "*.csv")
python scripts/select_subjects.py
