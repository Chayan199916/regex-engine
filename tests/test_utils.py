import pytest
from regex_engine.utils import (
    match_digit, match_alphabets, match_alphanum,
    match_pcg, match_ncg, is_ncgp, is_pcgp,
    is_alphap, is_digitp, match_character
)


def test_match_digit():
    assert match_digit('5') == True
    assert match_digit('a') == False


def test_match_alphabets():
    assert match_alphabets('a') == True
    assert match_alphabets('Z') == True
    assert match_alphabets('5') == False


def test_match_alphanum():
    assert match_alphanum('a') == True
    assert match_alphanum('5') == True
    assert match_alphanum('_') == True
    assert match_alphanum('!') == False


def test_match_pcg():
    assert match_pcg('a', 'abc') == True
    assert match_pcg('d', 'abc') == False


def test_match_ncg():
    assert match_ncg('d', 'abc') == True
    assert match_ncg('a', 'abc') == False


def test_is_ncgp():
    assert is_ncgp('[^abc]') == True
    assert is_ncgp('[abc]') == False


def test_is_pcgp():
    assert is_pcgp('[abc]') == True


def test_is_alphap():
    assert is_alphap('\\w') == True
    assert is_alphap('\\d') == False


def test_is_digitp():
    assert is_digitp('\\d') == True
    assert is_digitp('\\w') == False


def test_match_character():
    assert match_character('a', 'a') == True
    assert match_character('b', 'a') == False
    assert match_character('a', '[abc]') == True
    assert match_character('d', '[^abc]') == True
    assert match_character('5', '\\d') == True
    assert match_character('a', '\\w') == True
    assert match_character('a', '.') == True
