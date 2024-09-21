import pytest
from regex_engine.parser import parse


def test_parse_simple():
    assert parse('abc') == ['a', 'b', 'c']


def test_parse_digit():
    assert parse('\\d') == ['\\d']


def test_parse_word():
    assert parse('\\w') == ['\\w']


def test_parse_positive_character_group():
    assert parse('[abc]') == ['[abc]']


def test_parse_negative_character_group():
    assert parse('[^abc]') == ['[^abc]']


def test_parse_mixed():
    assert parse('a\\d[bc]\\w[^xyz]') == ['a', '\\d', '[bc]', '\\w', '[^xyz]']


def test_parse_quantifiers():
    assert parse('a+b?c*') == ['a', '+', 'b', '?', 'c', '*']


def test_parse_parentheses():
    assert parse('(a|b)c') == ['(', 'a', '|', 'b', ')', 'c']


def test_parse_complex():
    assert parse('^a\\d+[bc]?(x|y)*z$') == ['^', 'a', '\\d',
                                            '+', '[bc]', '?', '(', 'x', '|', 'y', ')', '*', 'z', '$']
