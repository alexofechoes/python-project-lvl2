# -*- coding:utf-8 -*-

"""Module with renderers from diff_ast."""
import json

from gendiff.nodetypes import PARENT


def format_ast(diff_ast):
    """Test message diff from diff_ast function result."""
    filtered_ast = _build_dict(diff_ast)
    return json.dumps(filtered_ast)


def _build_dict(ast):
    result = {}
    for key, node in ast.items():
        if node['type'] == PARENT:
            result[key] = _build_dict(node['children'])
        else:
            result[key] = node
    return result
