from rich.text import Text
from prppal.console import console
import pandas as pd
import time
from rich.progress import Spinner

def analyse(dfs):

    patrol_df = dfs[0]
    awards_df = dfs[1]

    # Example Analysis: Total hours per member
    # total_hours = patrol_df.groupby("Member ID")["Member Hours"].sum()
    # print(total_hours)

    # Example: Count of awards per member
    #awards_count = awards_df.groupby("Member ID")["Award Name"].count()
    #print(awards_count)

    grommets(patrol_df)
    rookies()
    jaffas()
    eagles()

"""
All members who took part in something called grommet patrol. idk if 
that actually classifies a grommet but just a test
"""
def grommets(patrol_df):
    with console.status("[yellow]Resolving [bold]Grommet[/bold] Members\n[/yellow]", spinner="dots"):

        grommet_members = patrol_df[patrol_df['Patrol Log Name'].str.contains('grommet', case=False, na=False)]

        # List member IDs for grommets
        grommet_member_ids = grommet_members['Member ID'].unique()

        console.log("Found [bold]Grommet[/bold] members with the following Member IDs:\n", style="green")
        for member_id in grommet_member_ids:
            console.log(f"- {member_id}", style="green")



def rookies():
    with console.status("[yellow]Resolving [bold]Rookie [/bold]members...\n[/yellow]", spinner="dots"):

        console.log("Found [bold]Rookie[/bold] members with the following Member IDs:\n", style="green")


def jaffas():
    with console.status("[yellow]Resolving [bold]Jaffa [/bold]members...\n[/yellow]", spinner="dots"):

        console.log("Found [bold]Jaffa[/bold] members with the following Member IDs:\n", style="green")
def eagles():
    with console.status("[yellow]Resolving [bold]Eagle [/bold]members...\n[/yellow]", spinner="dots"):

        console.log("Found [bold]Eagle [/bold] members with the following Member IDs:\n", style="green")
