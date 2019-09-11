# -*- coding:utf-8 -*-

import pytest

from gendiff.diff import dict_diff, generate_diff


def test_dict_diff():
    first = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22'}
    second = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    diff = dict_diff(first, second)

    assert diff == {
        'added': {'verbose': True},
        'removed': {'proxy': '123.234.53.22'},
        'changed': {'timeout': {'new': 20, 'old': 50}},
        'unchanged': {'host': 'hexlet.io'},
    }


def test_message_from_diff(expected_plain):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
    )
    assert diff.split('\n') == expected_plain


@pytest.fixture
def expected_plain(request):
    with open('tests/fixtures/expected_plain.txt') as file:
        yield file.read().splitlines()
