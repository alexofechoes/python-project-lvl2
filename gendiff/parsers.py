# -*- coding:utf-8 -*-

"""Module for parsing raw_text files to dict."""
import json

import yaml

parsers = {
    'json': lambda data: json.loads(data),
    'yaml': lambda data: yaml.safe_load(data),
}


def parse(file_extension: str, raw_data: str):
    """Parse raw text data to dict."""
    parse_func = _create_parse_func(file_extension)
    return parse_func(raw_data)


def _create_parse_func(file_extension: str):
    if file_extension == 'yml':
        file_extension = 'yaml'

    if file_extension not in parsers:
        raise AttributeError(
            'File extension {file_extension} not supported'.format(
                file_extension=file_extension,
            ),
        )

    return parsers[file_extension]
