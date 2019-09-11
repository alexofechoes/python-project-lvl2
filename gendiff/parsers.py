# -*- coding:utf-8 -*-

"""Module for parsing raw_text files to dict."""
import json

import yaml

parsers = {
    'json': lambda data: json.loads(data),
    'yaml': lambda data: yaml.safe_load(data),
}


def parse(data_format, raw_data):
    """Parse raw text data to dict."""
    parse_func = _create_parse_func(data_format)
    return parse_func(raw_data)


def _create_parse_func(data_format):
    if data_format == 'yml':
        data_format = 'yaml'

    if data_format not in parsers:
        raise AttributeError(
            'Format {format} not supported'.format(format=data_format),
        )

    return parsers[data_format]
