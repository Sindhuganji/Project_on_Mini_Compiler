import re

TOKEN_SPEC = [
    ('COMMENT',  r'\#.*'),
    ('STRING',   r'"[^"]*"'),
    ('NUMBER',   r'\d+'),
    ('LE',       r'<='),
    ('GE',       r'>='),
    ('EQ',       r'=='),
    ('NE',       r'!='),
    ('LT',       r'<'),
    ('GT',       r'>'),
    ('ID',       r'[a-zA-Z_]\w*'),
    ('ASSIGN',   r'='),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('MULT',     r'\*'),
    ('DIV',      r'/'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('NEWLINE',  r'\n'),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.')
]

token_regex = '|'.join(f'(?P<{n}>{p})' for n, p in TOKEN_SPEC)

def tokenize(code):
    tokens = []
    line = 1

    for m in re.finditer(token_regex, code):
        kind = m.lastgroup
        value = m.group()

        if kind == 'NEWLINE':
            line += 1
            continue
        if kind in ('SKIP', 'COMMENT'):
            continue
        if kind == 'NUMBER':
            tokens.append(('NUMBER', int(value), line))
        elif kind == 'STRING':
            tokens.append(('STRING', value[1:-1], line))
        elif kind == 'ID':
            tokens.append(('ID', value, line))
        elif kind == 'MISMATCH':
            raise RuntimeError(f"Unexpected character '{value}' at line {line}")
        else:
            tokens.append((kind, value, line))

    return tokens