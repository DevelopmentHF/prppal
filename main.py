import argparse 
from prppal.data_extraction import extract
from prppal.analysis import analyse
from rich.text import Text
from prppal.console import console
import time

def main():
    
    console.log(Text("Started prppal...\n", style="green"))
    time.sleep(0.25)
    parser = argparse.ArgumentParser(description="Add file names to perform PRP analysis on.")
    parser.add_argument("--patrols", type=str, help=".csv file containing patrolling data")
    parser.add_argument("--awards", type=str, help=".csv file containing qualification and award data")

    args = parser.parse_args()

    analyse(extract(args))


if __name__ == "__main__":
    main()
