import numpy as np
import pandas as pd
import scipy.sparse as sparse

print("Reading in pickled sparse dataframe.")
df = pd.read_pickle('output/hansen666.matrix.pkl')

print("Converting to a LIL sparse matrix.")
df_lil = sparse.lil_matrix(df.to_coo())
(_, n_subjects) = df_lil.shape

out_df = pd.DataFrame(index=df.index)

out_df['count'] = np.floor(df_lil.sum(axis=1))

for n_subjects_to_select in [5, 10, 50, 100, 500]:
    print(f"Selecting {n_subjects_to_select} subjects...")
    selected_subjects = np.random.choice(n_subjects, n_subjects_to_select, replace=False)
    # np.floor used here just for type conversion
    out_df[f'count_in_{n_subjects_to_select}'] = np.floor(df_lil[:, tuple(selected_subjects)].sum(axis=1))

out_df.to_csv('output/hansen666.subject_subsampled.csv.bz2', compression='bz2')
