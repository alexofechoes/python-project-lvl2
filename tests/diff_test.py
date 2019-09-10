from gendiff.diff import dict_diff
from gendiff.diff import generate_diff_from_dicts


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


def test_message_from_diff():
    first = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22'}
    second = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    result = generate_diff_from_dicts(first, second)
    expected = """{
    host: hexlet.io
  + timeout: 20
  - timeout: 50
  - proxy: 123.234.53.22
  + verbose: True
}"""

    assert result.split('\n') == expected.split('\n')
