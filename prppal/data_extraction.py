import pandas as pd


def extract(filepath_args):
    print(f'extracting data from {filepath_args.patrols} & {filepath_args.awards}')

    # load the CSV files
    patrol_df = pd.read_csv(filepath_args.patrols, header=1) # first row is garbage
    print(patrol_df.columns)
    awards_df = pd.read_csv(filepath_args.awards)

    # merge on Member ID, the same in both csvs
    merged_df = pd.merge(patrol_df, awards_df, on="Member ID", how="inner")

    # Example Analysis: Total hours per member
    total_hours = patrol_df.groupby("Member ID")["Member Hours"].sum()
    print(total_hours)

    # Example: Count of awards per member
    #awards_count = awards_df.groupby("Member ID")["Award Name"].count()
    #print(awards_count)
