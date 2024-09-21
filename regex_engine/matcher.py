from typing import List
from .utils import match_character, create_char_matcher
from .parser import parse


def match_pattern(text: str, pattern: str) -> bool:
    regex = parse(pattern)
    if regex and regex[0] == "^":
        return match_here(text, regex[1:])
    while text:
        if match_here(text, regex):
            return True
        text = text[1:]
    return False


def match_here(text: str, regex: List[str]) -> bool:
    if not regex:
        return True
    if len(regex) == 1 and regex[0] == "$":
        return not text
    if len(regex) == 1:
        return bool(text) and match_character(text[0], regex[0])
    if len(regex) >= 2 and regex[1] in ("+", "?"):
        return match_quantifier(regex[0], text, regex[2:], regex[1])
    if len(regex) >= 2 and regex[0] == "(" and ")" in regex:
        return match_group(text, regex)
    if text and match_character(text[0], regex[0]):
        return match_here(text[1:], regex[1:])
    return False


def match_quantifier(char: str, text: str, regex: List[str], quantifier: str) -> bool:
    char_matcher = create_char_matcher(char)
    if quantifier == "+":
        if not text or not char_matcher(text[0]):
            return False
    while text and char_matcher(text[0]):
        text = text[1:]
    return match_here(text, regex)


def match_group(text: str, regex: List[str]) -> bool:
    end_index = regex.index(")")
    or_patterns = [parse(r) for r in "".join(regex[1:end_index]).split("|")]
    after_part = regex[end_index + 1:]
    return any(match_here(text, pattern + after_part) for pattern in or_patterns)
