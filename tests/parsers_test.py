# -*- coding:utf-8 -*-

import pytest

from gendiff import parsers


def test_json_parse():
    json_data = """
{
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22"
}
"""
    expected = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
    }

    assert parsers.parse_json(json_data) == expected


def test_yaml_parse():
    yaml_data = """
        host: hexlet.io
        timeout: 50
        proxy: "123.234.53.22"
"""
    expected = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
    }

    assert parsers.parse_yaml(yaml_data) == expected
