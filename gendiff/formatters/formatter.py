# -*- coding:utf-8 -*-

"""Facade for ast formatters."""
from gendiff.formatters import json, plain, text

formats = {
    'json': json.format_ast,
    'plain': plain.format_ast,
    'text': text.format_ast,
}


def format_ast(ast, result_format):
    """Format from ast to result format."""
    if result_format not in formats:
        raise AttributeError(
            'Result format {format} not supported'.format(format=result_format),
        )
    format_func = formats[result_format]
    return format_func(ast)
