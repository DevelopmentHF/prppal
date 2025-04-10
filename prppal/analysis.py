from rich.text import Text
from prppal.console import console
import pandas as pd
import time
from rich.progress import Spinner

def analyse(dfs):

    patrol_df = dfs[0]
    awards_df = dfs[1]

    # convert date to datetime pandas format
    patrol_df['Patrol Date'] = pd.to_datetime(patrol_df['Patrol Date'], format='%a %d/%m/%Y')
    #print(patrol_df)

    # create new column for fiscal year
    patrol_df['fiscal_year'] = patrol_df['Patrol Date'].apply(get_fiscal_year)

    grommet_members_df = grommets(patrol_df, awards_df)

    rookie_members_df = rookies(patrol_df, awards_df)

    patrol_hours_for_each_year_df = patrol_df.groupby(['Member ID', 'fiscal_year'])['Member Hours'].sum().reset_index()
    
    jaffa_members_df = jaffas(rookie_members_df, patrol_hours_for_each_year_df, required_hours_per_year=20)
    
    eagles()

    # If a member is a rookie, they are not a grommet
    grommet_members_df = grommet_members_df[~grommet_members_df['Member ID'].isin(rookie_members_df['Member ID'])]

    # If a member is a jaffa, they are not a rookie
    rookie_members_df = rookie_members_df[~rookie_members_df['Member ID'].isin(jaffa_members_df['Member ID'])]

    # display grommets info
    console.log(f"Number of [bold]Grommets[/bold]: {len(grommet_members_df)}\n", style="green")
    console.log("Found [bold]Grommet[/bold] members with the following Member IDs:\n", style="green")
    for member_id in grommet_members_df['Member ID']:
        console.log(f"- {member_id}", style="green")

    # display rookies info
    console.log(f"Number of [bold]Rookies[/bold]: {len(rookie_members_df)}\n", style="green")
    console.log("Found [bold]Rookie[/bold] members with the following Member IDs:\n", style="green")
    for member_id in rookie_members_df['Member ID']:
        console.log(f"- {member_id}", style="green")

    # display jaffas info
    console.log(f"Number of [bold]Jaffas[/bold]: {len(jaffa_members_df)}\n", style="green")
    console.log("Found [bold]Jaffa[/bold] members with the following Member IDs:\n", style="green")
    for member_id in jaffa_members_df['Member ID']:
        console.log(f"- {member_id}", style="green")

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

        return pd.DataFrame(grommet_member_ids, columns=['Member ID'])



def rookies(patrol_df, awards_df):
    with console.status("[yellow]Resolving [bold]Rookie [/bold]members...\n[/yellow]", spinner="dots"):

        # must have the bronze medallion
        rookie_members = awards_df[awards_df['Award Name'].str.contains('bronze medallion', case=False, na=False)]

        # List member IDs for rookies
        rookie_member_ids = rookie_members['Member ID'].unique()

        unique_members = rookie_members[['Member ID']].drop_duplicates().reset_index(drop=True)

        return unique_members


def jaffas(rookie_members_df, patrol_hours_for_each_year_df, required_hours_per_year):
    with console.status("[yellow]Resolving [bold]Jaffa [/bold]members...\n[/yellow]", spinner="dots"):

        jaffas_df = []

        num_years_with_20_hours = 0
        prev_member_id = None
        if len(patrol_hours_for_each_year_df) > 0:
            prev_member_id = patrol_hours_for_each_year_df.iloc[0]['Member ID']
        else:
            return

        for index, row in patrol_hours_for_each_year_df.iterrows():
            # are we still looking at the same member?
            if row['Member ID'] == prev_member_id:

                # does the member have 20 or more hours for this fiscal year?
                if row['Member Hours'] >= required_hours_per_year:
                    num_years_with_20_hours += 1

                # does this member have 2 or more years with over 20 hours?
                if num_years_with_20_hours >= 2 and row['Member ID'] not in jaffas_df and row['Member ID'] in rookie_members_df['Member ID'].values:
                    jaffas_df.append(row['Member ID'])

            else:
                # we are looking at the first fiscal year of the next member
                prev_member_id = row['Member ID']
                num_years_with_20_hours = 0

                if row['Member Hours'] >= required_hours_per_year:
                    num_years_with_20_hours += 1

        jaffas_df = pd.DataFrame(jaffas_df, columns=['Member ID'])
        jaffas_df['Member ID'] = jaffas_df['Member ID'].astype(int)

        return jaffas_df

def eagles():
    with console.status("[yellow]Resolving [bold]Eagle [/bold]members...\n[/yellow]", spinner="dots"):

        console.log("Found [bold]Eagle [/bold] members with the following Member IDs:\n", style="green")

# Function to get fiscal year
def get_fiscal_year(date):
    if date.month >= 7:  # If the month is July or later, it's the current fiscal year
        return date.year
    else:  # If before July, it's the previous fiscal year
        return date.year - 1
