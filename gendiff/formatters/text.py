# -*- coding:utf-8 -*-

"""Text formatter from ast."""
from typing import Any, Dict

from gendiff import ast

_SYMBOLS = {
    ast.ADDED: '+',
    ast.REMOVED: '-',
    ast.UNCHANGED: ' ',
}


def format_ast(ast_diff: Dict[str, Any]) -> str:
    """Format ast_diff to text string."""
    return '{{\n{message}\n}}'.format(
        message=_build_message(ast_diff),
    )


def _build_message(ast_diff: Dict[str, Any], depth: int = 0) -> str:
    message_lines = []
    for key, node in sorted(ast_diff.items(), key=lambda item: item[0]):
        node_type = node[ast.TYPE]
        if node_type == ast.PARENT:
            children = _build_message(node[ast.CHILDREN], depth=depth + 1)
            line = '    {indent}{key}: {{\n{children}\n    {indent}}}'.format(
                children=children,
                key=key,
                indent=_get_indent(depth),
            )
        elif node_type == ast.CHANGED:
            line = '{added}\n{removed}'.format(
                added=_get_message(ast.ADDED, key, node[ast.VALUE], depth),
                removed=_get_message(
                    ast.REMOVED,
                    key,
                    node[ast.OLD_VALUE],
                    depth,
                ),
            )
        else:
            line = _get_message(node_type, key, node[ast.VALUE], depth)
        message_lines.append(line)
    return '\n'.join(message_lines)


def _get_message(node_type: str, key: str, value: Any, depth: int) -> str:
    return '{indent}  {symbol} {key}: {value}'.format(
        symbol=_SYMBOLS.get(node_type, ' '),
        key=key,
        value=_get_value(value, depth + 1),
        indent=_get_indent(depth),
    )


def _get_value(value: Any, depth: int):
    if isinstance(value, dict):
        return _get_dict_value(value, depth)
    return value


def _get_dict_value(sub_dict: Dict[str, Any], depth: int) -> str:
    res = []
    for key, value in sub_dict.items():
        res.append('{{\n    {indent}{key}: {value}\n{indent}}}'.format(
            key=key,
            value=value,
            indent=_get_indent(depth),
        ))
    return '\n'.join(res)


def _get_indent(depth: int) -> str:
    return '    ' * depth
