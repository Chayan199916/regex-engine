import pytest
from regex_engine.matcher import match_pattern


@pytest.mark.parametrize("pattern,text,expected", [
    ('abc', 'abc', True),
    ('abc', 'abd', False),
    ('^abc', 'abc', True),
    ('^abc', 'dabc', False),
    ('abc$', 'abc', True),
    ('abc$', 'abcd', False),
    ('\\d', '5', True),
    ('\\d', 'a', False),
    ('\\w', 'a', True),
    ('\\w', '!', False),
    ('[abc]', 'b', True),
    ('[abc]', 'd', False),
    ('[^abc]', 'd', True),
    ('[^abc]', 'a', False),
    ('a+', 'aaa', True),
    ('a+', 'b', False),
    ('a?', 'a', True),
    ('a?', 'aa', True),
    ('(x|y)', 'x', True),
    ('(x|y)', 'y', True),
    ('(x|y)', 'z', False),
    ('a\\d[bc]?(x|y)z', 'a5bcxz', True)
])
def test_match_pattern(pattern, text, expected):
    assert match_pattern(text, pattern) == expected


def test_match_pattern_edge_cases():
    assert match_pattern('^$', '') == True
    assert match_pattern('^$', 'nonempty') == False
