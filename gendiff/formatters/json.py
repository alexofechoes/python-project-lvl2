# -*- coding:utf-8 -*-

"""Json formatter from ast."""
import json
from typing import Any, Dict

from gendiff import ast


def format_ast(ast_diff: Dict[str, Any]) -> str:
    """Format ast to json string."""
    filtered_ast = _build_dict(ast_diff)
    return json.dumps(filtered_ast)


def _build_dict(ast_diff: Dict[str, Any]) -> Dict[str, Any]:
    result = {}
    for key, node in ast_diff.items():
        if node[ast.TYPE] == ast.PARENT:
            result[key] = _build_dict(node[ast.CHILDREN])
        else:
            result[key] = node
    return result
