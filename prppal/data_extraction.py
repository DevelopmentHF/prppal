import pandas as pd
from rich.text import Text
from prppal.console import console


def extract(filepath_args):
    message = Text()
    message.append("Attempting to extract data from ", style="yellow")
    message.append(filepath_args.patrols, style="bold green")
    message.append(" & ", style="yellow")
    message.append(filepath_args.awards + "\n", style="bold green")
    console.log(message)

    # load the CSV files
    patrol_df = pd.read_csv(filepath_args.patrols, header=1) # first row is garbage
    awards_df = pd.read_csv(filepath_args.awards)

    console.log("Files successfully loaded\n", style="green")

    # merge on Member ID, the same in both csvs
    merged_df = pd.merge(patrol_df, awards_df, on="Member ID", how="inner")

    return patrol_df, awards_df
