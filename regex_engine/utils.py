from typing import Callable


def match_digit(char: str) -> bool:
    return ord("0") <= ord(char) <= ord("9")


def match_alphabets(char: str) -> bool:
    is_upper = ord("A") <= ord(char) <= ord("Z")
    is_lower = ord("a") <= ord(char) <= ord("z")
    return is_upper or is_lower


def match_alphanum(char: str) -> bool:
    return match_alphabets(char) or match_digit(char) or char == "_"


def match_pcg(char: str, group: str) -> bool:
    return char in group


def match_ncg(char: str, group: str) -> bool:
    return char not in group


def is_ncgp(pattern: str) -> bool:
    return len(pattern) >= 4 and pattern[0:2] == "[^" and pattern[-1] == "]"


def is_pcgp(pattern: str) -> bool:
    return len(pattern) >= 3 and pattern[0] == "[" and pattern[-1] == "]"


def is_alphap(pattern: str) -> bool:
    return pattern == "\\w"


def is_digitp(pattern: str) -> bool:
    return pattern == "\\d"


def match_character(char: str, pattern: str) -> bool:
    if is_ncgp(pattern):
        return match_ncg(char, pattern[2:-1])
    if is_pcgp(pattern):
        return match_pcg(char, pattern[1:-1])
    if is_alphap(pattern):
        return match_alphanum(char)
    if is_digitp(pattern):
        return match_digit(char)
    if pattern == ".":
        return bool(char)
    return pattern == char


CharMatcher = Callable[[str], bool]


def create_char_matcher(pattern: str) -> CharMatcher:
    return lambda char: match_character(char, pattern)
