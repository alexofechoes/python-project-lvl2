# -*- coding:utf-8 -*-

"""Text formatter from ast."""
from gendiff.ast import ADDED, CHANGED, PARENT, REMOVED, UNCHANGED


def format_ast(ast):
    """Format ast to text string."""
    return '{{\n{message}\n}}'.format(
        message=_build_message(ast),
    )


def _build_message(ast, depth=0):
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
        if node['type'] == CHANGED:
            line = '{added}\n{removed}'.format(
                added=_get_message(
                    symbol='+',
                    key=key,
                    value=node['value'],
                    depth=depth,
                ),
                removed=_get_message(
                    symbol='-',
                    key=key,
                    value=node['oldValue'],
                    depth=depth,
                ),
            )
        if node['type'] == UNCHANGED:
            line = _get_message(
                symbol=' ',
                key=key,
                value=node['value'],
                depth=depth,
            )
        if node['type'] == ADDED:
            line = _get_message(
                symbol='+',
                key=key,
                value=node['value'],
                depth=depth,
            )
        if node['type'] == REMOVED:
            line = _get_message(
                symbol='-',
                key=key,
                value=node['value'],
                depth=depth,
            )
        message_lines.append(line)
    return '\n'.join(message_lines)


def _get_message(symbol, key, value, depth):
    return '{indent}  {symbol} {key}: {value}'.format(
        symbol=symbol,
        key=key,
        value=_get_value(value, depth + 1),
        indent=_get_indent(depth),
    )


def _get_value(value, depth):
    if isinstance(value, dict):
        return _get_dict_value(value, depth)
    return value


def _get_dict_value(sub_dict, depth):
    res = []
    for key, value in sub_dict.items():
        res.append('{{\n    {indent}{key}: {value}\n{indent}}}'.format(
            key=key,
            value=value,
            indent=_get_indent(depth),
        ))
    return '\n'.join(res)


def _get_indent(depth):
    return '    ' * depth
