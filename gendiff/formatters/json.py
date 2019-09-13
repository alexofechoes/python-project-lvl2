# -*- coding:utf-8 -*-

"""Json formatter from ast."""
import json
from typing import Any, Dict

from gendiff.ast import PARENT


def format_ast(ast: Dict[str, Any]) -> str:
    """Format ast to json string."""
    filtered_ast = _build_dict(ast)
    return json.dumps(filtered_ast)


def _build_dict(ast: Dict[str, Any]) -> Dict[str, Any]:
    result = {}
    for key, node in ast.items():
        if node['type'] == PARENT:
            result[key] = _build_dict(node['children'])
        else:
            result[key] = node
    return result
