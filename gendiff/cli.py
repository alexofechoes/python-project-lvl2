# -*- coding:utf-8 -*-

"""Cli module."""
import argparse

from gendiff import generate_diff
from gendiff.formatters import json, plain, text

_FORMATS = {
    'json': json.format_ast,
    'plain': plain.format_ast,
    'text': text.format_ast,
}

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument(
    '-f',
    '--format',
    dest='FORMAT',
    choices=_FORMATS,
    default='text',
    help='set format of output',
)
parser.add_argument('first_file', metavar='FIRST_FILE')
parser.add_argument('second_file', metavar='SECOND_FILE')


def main():
    """Run cli."""
    args = parser.parse_args()
    diff = generate_diff(
        args.first_file,
        args.second_file,
        format_func=_FORMATS[args.FORMAT],
    )
    print(diff)


if __name__ == '__main__':
    main()
