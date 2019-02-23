import click
import numpy as np
import os
import pandas as pd

from collections import Counter


def counted_lines_of_file(path):
    """
    Return a dict keyed on the lines of the file, with values being the number
    of times that line was seen.
    """
    print(f"Reading {path}")
    with open(path) as fp:
        fp.readline()  # burn the header row
        counted = Counter(fp)
    return {k.rstrip(): v for k, v in counted.items()}


@click.command()
@click.option(
    '--out-path',
    type=click.Path(writable=True),
    help="Output path.",
    required=True)
@click.argument('in_paths', nargs=-1)
def sparse_count_df(out_path, in_paths):
    """
    Make a pickled sparse DataFrame out of all the input files.

    Specifically, each line in the union of the files gets a row, and each file
    gets a column. The entries count the number of times that line showed up in
    that file.
    """

    data = {
        os.path.basename(path): counted_lines_of_file(path)
        for path in in_paths
    }

    all_keys_set = set()

    for _, d in data.items():
        all_keys_set = all_keys_set.union(d.keys())

    all_keys = np.array(list(all_keys_set))

    def series_of_dict(d):
        s = pd.Series(index=all_keys)
        for k, v in d.items():
            s[k] = v
        return s

    df = pd.SparseDataFrame(index=all_keys, )
    for k, v in data.items():
        print(f"Putting {k} into sparse data frame.")
        df[k] = series_of_dict(v)

    df.to_pickle(out_path)
    click.echo(f"Density: {df.density}")


if __name__ == '__main__':
    sparse_count_df()
