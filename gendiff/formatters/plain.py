# -*- coding:utf-8 -*-

"""Plain formatter from ast."""
from typing import Any, Dict, List, Optional

from gendiff.ast import ADDED, CHANGED, PARENT, REMOVED


def format_ast(ast: Dict[str, Any]) -> str:
    """Format ast to plain string."""
    return _build_message(ast)


def _build_message(
    ast: Dict[str, Any],
    parents: Optional[List[str]] = None,
) -> str:
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


def _get_value(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return 'complex value'
    return str(value)


def _get_path(parents: List[str], key: str) -> str:
    return '.'.join(parents + [key])
