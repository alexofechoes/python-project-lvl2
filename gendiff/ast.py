# -*- coding:utf-8 -*-

"""Module for create ast diff."""
ADDED = 'added'
REMOVED = 'removed'
CHANGED = 'changed'
UNCHANGED = 'unchanged'
PARENT = 'parent'


def build_ast(first, second):
    """Diff between first and second dicts."""
    first_keys = first.keys()
    second_keys = second.keys()

    add_keys = second_keys - first_keys
    remove_keys = first_keys - second_keys
    common_keys = first_keys & second_keys

    added = {
        key: {'type': ADDED, 'value': second[key]}
        for key in add_keys
    }
    removed = {
        key: {'type': REMOVED, 'value': first[key]}
        for key in remove_keys
    }

    common = {}
    for key in common_keys:
        if first[key] == second[key]:
            common[key] = {
                'type': UNCHANGED,
                'value': second[key],
            }
        elif isinstance(first[key], dict) and isinstance(second[key], dict):
            common[key] = {
                'type': PARENT,
                'children': build_ast(first[key], second[key]),
            }
        else:
            common[key] = {
                'type': CHANGED,
                'value': second[key],
                'oldValue': first[key],
            }

    return {**common, **added, **removed}
