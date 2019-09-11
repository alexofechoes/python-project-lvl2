# -*- coding:utf-8 -*-

"""Funtions for generate diff."""
import json


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


def _plain_message(diff):
    message_format = '  {symbol} {key}: {value}'

    unchanged_messages = [
        message_format.format(symbol=' ', key=key, value=value)
        for key, value in diff['unchanged'].items()
    ]
    changed_messages = sum(
        [
            [
                message_format.format(symbol='+', key=key, value=value['new']),
                message_format.format(symbol='-', key=key, value=value['old']),
            ]
            for key, value in diff['changed'].items()
        ],
        [],
    )
    removed_messages = [
        message_format.format(symbol='-', key=key, value=value)
        for key, value in diff['removed'].items()
    ]
    added_messages = [
        message_format.format(symbol='+', key=key, value=value)
        for key, value in diff['added'].items()
    ]

    message = [
        '{',
        *unchanged_messages,
        *changed_messages,
        *removed_messages,
        *added_messages,
        '}',
    ]
    return '\n'.join(message)


def generate_diff(path_to_file1: str, path_to_file2: str):
    """Generate message different two files."""
    with open(path_to_file1) as first_file:
        first_data = json.load(first_file)
    with open(path_to_file2) as second_file:
        second_data = json.load(second_file)

    diff = dict_diff(first_data, second_data)
    return _plain_message(diff)
