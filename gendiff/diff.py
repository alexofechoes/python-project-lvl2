# -*- coding:utf-8 -*-
import json


def dict_diff(first, second):
    first_keys = first.keys()
    second_keys = second.keys()

    add_keys = second_keys - first_keys
    remove_keys = first_keys - second_keys
    common_keys = first_keys & second_keys

    added = {key: second[key] for key in add_keys}
    removed = {key: first[key] for key in remove_keys}
    changed = {
        key: {'old': first[key], 'new': second[key]}
        for key in common_keys if first[key] != second[key]
    }
    unchanged = {
        key: first[key]
        for key in common_keys if first[key] == second[key]
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
    changed_messages = sum([
        [
            message_format.format(symbol='+', key=key, value=value['new']),
            message_format.format(symbol='-', key=key, value=value['old'])
        ]
        for key, value in diff['changed'].items()
    ], [])
    removed_messages = [
        message_format.format(symbol='-', key=key, value=value)
        for key, value in diff['removed'].items()
    ]
    added_messages = [
        message_format.format(symbol='+', key=key, value=value)
        for key, value in diff['added'].items()
    ]

    result = [
        '{',
        *unchanged_messages,
        *changed_messages,
        *removed_messages,
        *added_messages,
        '}'
    ]
    return '\n'.join(result)


def generate_diff_from_dicts(first, second):
    diff = dict_diff(first, second)
    return _plain_message(diff)


def generate_diff(path_to_file1, path_to_file2):
    first_data = json.load(open(path_to_file1))
    second_data = json.load(open(path_to_file2))
    return generate_diff_from_dicts(first_data, second_data)
