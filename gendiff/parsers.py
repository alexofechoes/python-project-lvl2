# -*- coding:utf-8 -*-

"""Module for parsing raw_text files to dict."""
import json
from typing import Any, Dict

import yaml


def parse_json(data: str) -> Dict[str, Any]:
    """Parse data from json format to dict."""
    return json.loads(data)


def parse_yaml(data: str) -> Any:
    """Parse data from yaml format to dict."""
    return yaml.safe_load(data)
