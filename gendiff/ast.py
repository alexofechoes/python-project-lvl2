# -*- coding:utf-8 -*-

"""Module for create ast diff."""
from typing import Any, Dict

TYPE = 'type'
CHILDREN = 'children'
VALUE = 'value'
OLD_VALUE = 'old_value'
ADDED = 'added'
REMOVED = 'removed'
CHANGED = 'changed'
UNCHANGED = 'unchanged'
PARENT = 'parent'


def build_ast(first: Dict[str, Any], second: Dict[str, Any]) -> Dict[str, Any]:
    """Generate ast diff between first and second dicts."""
    first_keys = first.keys()
    second_keys = second.keys()

    add_keys = second_keys - first_keys
    remove_keys = first_keys - second_keys
    common_keys = first_keys & second_keys

    added = {
        key: {TYPE: ADDED, VALUE: second[key]}
        for key in add_keys
    }
    removed = {
        key: {TYPE: REMOVED, VALUE: first[key]}
        for key in remove_keys
    }

    common = {}
    for key in common_keys:
        first_item = first[key]
        second_item = second[key]
        if first_item == second_item:
            common[key] = {
                TYPE: UNCHANGED,
                VALUE: second_item,
            }
        elif isinstance(first_item, dict) and isinstance(second_item, dict):
            common[key] = {
                TYPE: PARENT,
                CHILDREN: build_ast(first_item, second_item),
            }
        else:
            common[key] = {
                TYPE: CHANGED,
                VALUE: second_item,
                OLD_VALUE: first_item,
            }

    return {**common, **added, **removed}
