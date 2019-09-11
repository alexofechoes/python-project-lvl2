# -*- coding:utf-8 -*-

"""Funtions for generate diff."""
from gendiff import formatters, parsers


def dict_diff(first, second):
    """Diff between first and second dicts."""
    first_keys = first.keys()
    second_keys = second.keys()

    add_keys = second_keys - first_keys
    remove_keys = first_keys - second_keys
    common_keys = first_keys & second_keys

    added = {key: second[key] for key in add_keys}
    removed = {key: first[key] for key in remove_keys}
    changed = {
        key: {'old': first[key], 'new': second[key]}
        for key in common_keys
        if first[key] != second[key]
    }
    unchanged = {
        key: first[key] for key in common_keys if first[key] == second[key]
    }

    return {
        'added': added,
        'removed': removed,
        'changed': changed,
        'unchanged': unchanged,
    }


def generate_diff(path_to_file1: str, path_to_file2: str):
    """Generate message different two files."""
    with open(path_to_file1) as first_file:
        first_data = parsers.parse(
            _format_data(path_to_file1),
            first_file.read(),
        )
    with open(path_to_file2) as second_file:
        second_data = parsers.parse(
            _format_data(path_to_file2),
            second_file.read(),
        )

    diff = dict_diff(first_data, second_data)
    return formatters.plain_message(diff)


def _format_data(path_to_file):
    return path_to_file.split('.')[-1]
