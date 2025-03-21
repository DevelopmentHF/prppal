from prppal.data_extraction import extract
from prppal.analysis import analyse


def main():
    print("Starting prppal...")
    extract()
    analyse()


if __name__ == "__main__":
    main()
