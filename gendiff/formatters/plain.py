# -*- coding:utf-8 -*-

"""Plain formatter from ast."""
from typing import Any, Dict, List, Optional

from gendiff import ast


def format_ast(ast_diff: Dict[str, Any]) -> str:
    """Format ast_diff to plain string."""
    return _build_message(ast_diff)


def _build_message(
    ast_diff: Dict[str, Any],
    parents: Optional[List[str]] = None,
) -> str:
    if not parents:
        parents = []

    message_lines = []
    for key, node in sorted(ast_diff.items(), key=lambda item: item[0]):
        node_type = node[ast.TYPE]

        if node_type == ast.PARENT:
            line = _build_message(node[ast.CHILDREN], parents=parents + [key])
        elif node_type == ast.CHANGED:
            message = "Property '{key}' was changed. From '{old}' to '{new}'"
            line = message.format(
                key=_get_path(parents, key),
                old=_get_value(node[ast.OLD_VALUE]),
                new=_get_value(node[ast.VALUE]),
            )
        elif node_type == ast.ADDED:
            message = "Property '{key_path}' was added with value: '{value}'"
            line = message.format(
                key_path=_get_path(parents, key),
                value=_get_value(node[ast.VALUE]),
            )
        elif node_type == ast.REMOVED:
            line = "Property '{key_path}' was removed".format(
                key_path=_get_path(parents, key),
            )
        else:
            continue

        message_lines.append(line)
    return '\n'.join(message_lines)


def _get_value(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return 'complex value'
    return str(value)


def _get_path(parents: List[str], key: str) -> str:
    return '.'.join(parents + [key])
