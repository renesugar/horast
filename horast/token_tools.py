"""Various helper functions to query and manipulate tokens."""

import io
import tokenize
import typing as t

Scope = t.NamedTuple('Scope', [('start', t.Tuple[int, int]), ('end', t.Tuple[int, int])])


def get_tokens(code: str) -> t.List[tokenize.TokenInfo]:
    assert isinstance(code, str), type(code)
    code_bytes = code.encode() # type: bytes
    with io.BytesIO(code_bytes) as code_bytes_reader:
        tokenizer = tokenize.tokenize(code_bytes_reader.readline)
        tokens = [token for token in tokenizer]
    return tokens


def get_comment_tokens(code: str) -> t.List[tokenize.TokenInfo]:
    return [token for token in get_tokens(code) if token.type is tokenize.COMMENT]


def get_token_locations(tokens: t.List[tokenize.TokenInfo]) -> t.List[t.Tuple[int, int]]:
    return [token.start for token in tokens]


def get_token_scopes(tokens: t.List[tokenize.TokenInfo]) -> t.List[Scope]:
    return [Scope(token.start, token.end) for token in tokens]
