from rich.text import Text
from prppal.console import console
import pandas as pd
import time
from rich.progress import Spinner

def analyse(dfs):

    patrol_df = dfs[0]
    awards_df = dfs[1]

    # sum the number of patrol hours for each member
    patrol_hours_summed_df = patrol_df.groupby('Member ID')['Member Hours'].sum().reset_index()
    print(patrol_hours_summed_df)

    # Example Analysis: Total hours per member
    # total_hours = patrol_df.groupby("Member ID")["Member Hours"].sum()
    # print(total_hours)

    # Example: Count of awards per member
    #awards_count = awards_df.groupby("Member ID")["Award Name"].count()
    #print(awards_count)

    grommets(patrol_df, awards_df)
    rookies(patrol_df, awards_df)
    jaffas()
    eagles()

"""
All members who took part in something called grommet patrol. idk if 
that actually classifies a grommet but just a test
"""
def grommets(patrol_df, awards_df):
    with console.status("[yellow]Resolving [bold]Grommet[/bold] Members\n[/yellow]", spinner="dots"):  

        # must have the SRC certificate
        grommet_members = awards_df[awards_df['Award Name'].str.contains('surf rescue certificate', case=False, na=False)]

        # List member IDs for grommets
        grommet_member_ids = grommet_members['Member ID'].unique()

        console.log("Found [bold]Grommet[/bold] members with the following Member IDs:\n", style="green")
        for member_id in grommet_member_ids:
            console.log(f"- {member_id}", style="green")



def rookies(patrol_df, awards_df):
    with console.status("[yellow]Resolving [bold]Rookie [/bold]members...\n[/yellow]", spinner="dots"):

        # must have the bronze medallion
        rookie_members = awards_df[awards_df['Award Name'].str.contains('bronze medallion', case=False, na=False)]

        # List member IDs for rookies
        rookie_member_ids = rookie_members['Member ID'].unique()

        console.log("Found [bold]Rookie[/bold] members with the following Member IDs:\n", style="green")
        for member_id in rookie_member_ids:
            console.log(f"- {member_id}", style="green")


def jaffas():
    with console.status("[yellow]Resolving [bold]Jaffa [/bold]members...\n[/yellow]", spinner="dots"):

        console.log("Found [bold]Jaffa[/bold] members with the following Member IDs:\n", style="green")
def eagles():
    with console.status("[yellow]Resolving [bold]Eagle [/bold]members...\n[/yellow]", spinner="dots"):

        console.log("Found [bold]Eagle [/bold] members with the following Member IDs:\n", style="green")
