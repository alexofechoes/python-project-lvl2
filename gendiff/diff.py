# -*- coding:utf-8 -*-

"""Funtions for generate diff."""
import os
from typing import Any

from gendiff import ast, parsers

_PARSERS = {
    'json': parsers.parse_json,
    'yaml': parsers.parse_yaml,
}


def generate_diff(file_path1: str, file_path2: str, format_func) -> str:
    """Generate message different two files."""
    first_data = _get_parsed_file_content(file_path1)
    second_data = _get_parsed_file_content(file_path2)

    diff = ast.build_ast(first_data, second_data)
    return format_func(diff)


def _get_parsed_file_content(file_path: str) -> Any:
    parse_func = _get_parse_func_for_file(file_path)
    file_content = _get_file_content(file_path)
    return parse_func(file_content)


def _get_file_content(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


def _get_parse_func_for_file(file_path: str) -> Any:
    ext = _get_file_extension(file_path)
    if ext not in _PARSERS:
        raise ValueError('File format {ext} not supported')
    return _PARSERS.get(ext)


def _get_file_extension(file_path: str) -> str:
    file_extension = os.path.splitext(file_path)[-1][1:]
    if file_extension == 'yml':
        file_extension = 'yaml'
    return file_extension
