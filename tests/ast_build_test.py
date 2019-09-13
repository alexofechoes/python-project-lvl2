# -*- coding:utf-8 -*-

from gendiff.ast import ADDED, CHANGED, PARENT, REMOVED, UNCHANGED, build_ast


def test_ast_build():
    first = {
        'common': {
            'setting1': 'Value 1',
            'setting2': '200',
            'setting3': True,
            'setting6': {
                'key': 'value',
            },
        },
        'group1': {
            'baz': 'bas',
            'foo': 'bar',
        },
        'group2': {
            'abc': '12345',
        },
        'test': 'test',
        'foo': 'bar',
    }
    second = {
        'common': {
            'setting1': 'Value 1',
            'setting3': True,
            'setting4': 'blah blah',
            'setting5': {
                'key5': 'value5',
            },
        },
        'group1': {
            'foo': 'bar',
            'baz': 'bars',
        },
        'group3': {
            'fee': '100500',
        },
        'test': 'test',
        'foo': 'baz',
    }
    diff = build_ast(first, second)

    assert diff == {
        'common': {
            'type': PARENT,
            'children': {
                'setting1': {
                    'type': UNCHANGED,
                    'value': 'Value 1',
                },
                'setting2': {
                    'type': REMOVED,
                    'value': '200',
                },
                'setting3': {
                    'type': UNCHANGED,
                    'value': True,
                },
                'setting4': {
                    'type': ADDED,
                    'value': 'blah blah',
                },
                'setting5': {
                    'type': ADDED,
                    'value': {'key5': 'value5'},
                },
                'setting6': {
                    'type': REMOVED,
                    'value': {'key': 'value'},
                },
            },
        },
        'group1': {
            'type': PARENT,
            'children': {
                'baz': {
                    'type': CHANGED,
                    'value': 'bars',
                    'oldValue': 'bas',
                },
                'foo': {'type': UNCHANGED, 'value': 'bar'},
            },
        },
        'group2': {
            'type': REMOVED,
            'value': {'abc': '12345'},
        },
        'group3': {
            'type': ADDED,
            'value': {'fee': '100500'},
        },
        'test': {'type': UNCHANGED, 'value': 'test'},
        'foo': {'type': CHANGED, 'value': 'baz', 'oldValue': 'bar'},
    }
