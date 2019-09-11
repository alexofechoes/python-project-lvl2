# -*- coding:utf-8 -*-

"""Module with formatters function from diff dict."""


def plain_message(diff):
    """Plain message diff from dict_diff function result."""
    message_format = '  {symbol} {key}: {value}'

    unchanged_messages = [
        message_format.format(symbol=' ', key=key, value=value)
        for key, value in diff['unchanged'].items()
    ]
    changed_messages = sum(
        [
            [
                message_format.format(symbol='+', key=key, value=value['new']),
                message_format.format(symbol='-', key=key, value=value['old']),
            ]
            for key, value in diff['changed'].items()
        ],
        [],
    )
    removed_messages = [
        message_format.format(symbol='-', key=key, value=value)
        for key, value in diff['removed'].items()
    ]
    added_messages = [
        message_format.format(symbol='+', key=key, value=value)
        for key, value in diff['added'].items()
    ]

    message = [
        '{',
        *unchanged_messages,
        *changed_messages,
        *removed_messages,
        *added_messages,
        '}',
    ]
    return '\n'.join(message)
