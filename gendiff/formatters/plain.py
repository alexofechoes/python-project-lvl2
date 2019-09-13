# -*- coding:utf-8 -*-

"""Plain formatter from ast."""
from gendiff.ast import ADDED, CHANGED, PARENT, REMOVED


def format_ast(ast):
    """Format ast to plain string."""
    return _build_message(ast)


def _build_message(ast, parents=None):
    if not parents:
        parents = []

    message_lines = []
    for key in sorted(ast.keys()):
        node = ast[key]

        if node['type'] == PARENT:
            message_lines.append(
                _build_message(node['children'], parents=parents + [key]),
            )
        if node['type'] == CHANGED:
            message_lines.append(
                "Property '{key}' was changed. From '{old}' to '{new}'".format(
                    key=_get_path(parents, key),
                    old=_get_value(node['oldValue']),
                    new=_get_value(node['value']),
                ),
            )
        if node['type'] == ADDED:
            message_lines.append(
                "Property '{key_path}' was added with value: '{value}'".format(
                    key_path=_get_path(parents, key),
                    value=_get_value(node['value']),
                ),
            )
        if node['type'] == REMOVED:
            message_lines.append("Property '{key_path}' was removed".format(
                key_path=_get_path(parents, key),
            ))
    return '\n'.join(message_lines)


def _get_value(value):
    if isinstance(value, dict):
        return 'complex value'
    return value


def _get_path(parents, key):
    return '.'.join(parents + [key])
