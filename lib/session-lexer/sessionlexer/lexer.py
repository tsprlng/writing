# -*- coding: utf-8 -*-
"""
    pygments.lexers.shell
    ~~~~~~~~~~~~~~~~~~~~~

    Lexers for various shells.

    :copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import Lexer, RegexLexer, do_insertions, bygroups, \
    include, default, this, using, words
from pygments.token import Punctuation, \
    Text, Comment, Operator, Keyword, Name, String, Number, Generic
from pygments.util import shebang_matches


__all__ = ['SessionLexer']

line_re = re.compile('.*?\n')


class SessionLexer(RegexLexer):
    """
    Lexer for (ba|k|z|)sh shell scripts.

    .. versionadded:: 0.6
    """

    name = 'ShellSession'
    aliases = ['session']
    filenames = ['*.shellsession']
    mimetypes = ['application/x-shellsession']

    tokens = {
        'root': [
            (r'>>>', Comment, 'output'),
            (r'!>>', Comment, 'big-output'),
            (r' .*\n', Comment),
            (r'.*\n', Text),
        ],
        'output': [
            (r'.*\n', String, '#pop')
        ],
        'big-output': [
            (r'.*\n', Keyword, '#pop')
        ],
    }

    def analyse_text(text):
        if shebang_matches(text, r'(ba|z|)sh'):
            return 1
        if text.startswith('$ '):
            return 0.2
