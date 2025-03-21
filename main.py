import argparse 
from prppal.data_extraction import extract
from prppal.analysis import analyse


def main():
    print("Starting prppal...")

    parser = argparse.ArgumentParser(description="Add file names to perform PRP analysis on.")
    parser.add_argument("--patrols", type=str, help=".csv file containing patrolling data")
    parser.add_argument("--awards", type=str, help=".csv file containing qualification and award data")

    args = parser.parse_args()

    extract(args)
    analyse()


if __name__ == "__main__":
    main()
