import click
import pandas as pd
import numpy as np


def to_fake_csv(seq_list, path, include_freq=False):
    """
    Write a list of our favorite triples to a file.
    """
    with open(path, 'w') as fp:
        if include_freq:
            fp.write('amino_acid,v_gene,j_gene,frequency\n')
        else:
            fp.write('amino_acid,v_gene,j_gene\n')

        for line in seq_list:
            fp.write(line + '\n')


@click.command()
@click.option(
    '--include-freq',
    is_flag=True,
    help="Include frequencies as a column in CSV.")
@click.option(
    '--n-to-sample', default=100, help="Number of sequences to sample.")
@click.option(
    '--column',
    default='count',
    help="Counts column to use for sampling probabilities.")
@click.argument('in_csv')
@click.argument('out_csv')
def sample_data_set(include_freq, n_to_sample, column, in_csv, out_csv):
    """
    Sample sequences according to the counts given in the specified column and
    then output in a CSV file.
    """
    df = pd.read_csv(in_csv, index_col=0)

    # This is the total number of occurrences of each sequence in selected_m.
    seq_counts = np.array(df[column])
    seq_freqs = seq_counts / sum(seq_counts)
    sampled_seq_v = np.random.multinomial(n_to_sample, seq_freqs)

    if include_freq:
        df.reset_index(inplace=True)
        out_vect = df['index'] + ',' + seq_freqs.map(str)
    else:
        out_vect = df.index

    # In order to get the correct count, we take those that appear once or
    # more, then those twice or more, etc, until we exceed the maximum entry.
    sampled_seqs = []
    for i in range(np.max(sampled_seq_v)):
        sampled_seqs += list(out_vect[sampled_seq_v > i])

    to_fake_csv(sampled_seqs, out_csv)


if __name__ == '__main__':
    sample_data_set()
