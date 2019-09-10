# -*- coding:utf-8 -*-
import argparse
from gendiff import generate_diff


def main():
    """Run cli."""
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument(
        "-f", "--format", dest="FORMAT", help="set format of output"
    )
    parser.add_argument("first_file", metavar="first_file")
    parser.add_argument("second_file", metavar="second_file")

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
