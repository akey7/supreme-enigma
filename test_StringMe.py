import pytest
from StringMe import StringMe

def test_reflect():
    expected = "hello"
    instance = StringMe(expected)
    actual = instance.reflect()
    assert expected == actual


@pytest.mark.parametrize('test, expected', [
    ("", True),
    (" ", True),
    ("x", True),
    ("aba", True),
    ("yvvy", True),
    ("xyz", False)
])
def test_palindrome(test, expected):
    instance = StringMe(test)
    actual = instance.isPalindrome()
    assert expected == actual
