# -*- coding:utf-8 -*-

"""Funtions for generate diff."""
from gendiff import ast, formatters, parsers


def generate_diff(path_to_file1: str, path_to_file2: str, format_result: str):
    """Generate message different two files."""
    with open(path_to_file1) as first_file:
        first_data = parsers.parse(
            _get_file_extension(path_to_file1),
            first_file.read(),
        )
    with open(path_to_file2) as second_file:
        second_data = parsers.parse(
            _get_file_extension(path_to_file2),
            second_file.read(),
        )

    diff = ast.build_ast(first_data, second_data)
    return formatters.format_ast(diff, format_result)


def _get_file_extension(path_to_file):
    return path_to_file.split('.')[-1]
