import pandas as pd


def clean(input_file1, input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df3 = df1.merge(df2,left_on="respondent_id",right_on="id")
    df4 = df3.dropna()
    df5 = df4[~df4["job"].str.contains('insurance|Insurance')]
    df6 = df5.drop(columns="id")
    return df6


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file1')
    parser.add_argument('input_file2')
    parser.add_argument('output')
    args = parser.parse_args()
    cleaned = clean(args.input_file1,args.input_file2)
    cleaned.to_csv(args.output, index=False)

