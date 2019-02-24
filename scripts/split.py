import click
import os
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command()
@click.option('--train-size', default=0.5, help="Data fraction to use for train.")
@click.argument('in_csv')
def split(train_size, in_csv):
    df = pd.read_csv(in_csv, index_col=0)
    (df1, df2) = train_test_split(df, train_size=train_size)
    base,_ = os.path.splitext(in_csv)
    df1.to_csv(base+'.train.csv.bz2', compression='bz2')
    df2.to_csv(base+'.test.csv.bz2', compression='bz2')


if __name__ == '__main__':
    split()
