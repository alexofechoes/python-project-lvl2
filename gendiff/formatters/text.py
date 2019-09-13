# -*- coding:utf-8 -*-

"""Text formatter from ast."""
from typing import Any, Dict, Optional

from gendiff.ast import ADDED, CHANGED, PARENT, REMOVED, UNCHANGED


def format_ast(ast: Dict[str, Any]) -> str:
    """Format ast to text string."""
    return '{{\n{message}\n}}'.format(
        message=_build_message(ast),
    )


def _build_message(ast: Dict[str, Any], depth: Optional[int] = 0) -> str:
    message_lines = []
    for key in sorted(ast.keys()):
        node = ast[key]
        if node['type'] == PARENT:
            children = _build_message(node['children'], depth=depth + 1)
            line = '    {indent}{key}: {{\n{children}\n    {indent}}}'.format(
                children=children,
                key=key,
                indent=_get_indent(depth),
            )
        elif node['type'] == CHANGED:
            line = '{added}\n{removed}'.format(
                added=_get_message(ADDED, key, node['value'], depth),
                removed=_get_message(REMOVED, key, node['oldValue'], depth),
            )
        else:
            line = _get_message(node['type'], key, node['value'], depth)
        message_lines.append(line)
    return '\n'.join(message_lines)


def _get_message(node_type: str, key: str, value: Any, depth: int) -> str:
    return '{indent}  {symbol} {key}: {value}'.format(
        symbol=_get_symbol_by_type(node_type),
        key=key,
        value=_get_value(value, depth + 1),
        indent=_get_indent(depth),
    )


def _get_symbol_by_type(node_type: str) -> str:
    symbol_by_type = {
        ADDED: '+',
        REMOVED: '-',
        UNCHANGED: ' ',
    }
    return symbol_by_type.get(node_type, ' ')


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
