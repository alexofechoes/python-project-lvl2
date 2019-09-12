# -*- coding:utf-8 -*-

"""Cli module."""
import argparse

from gendiff import generate_diff


def main():
    """Run cli."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        '-f',
        '--format',
        dest='FORMAT',
        default='text',
        help='set format of output',
    )
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')

    args = parser.parse_args()
    diff = generate_diff(
        args.first_file,
        args.second_file,
        format_result=args.FORMAT,
    )
    print(diff)


if __name__ == '__main__':
    main()
