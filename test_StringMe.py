import pytest
from StringMe import StringMe

def test_reflect():
    expected = "hello"
    instance = StringMe(expected)
    actual = instance.reflect()
    assert expected == actual


@pytest.mark.parametrize("test, expected", [
    ("", True),
    (" ", True),
    ("x", True),
    ("aba", True),
    ("yvvy", True),
    ("xyz", False)
])
def test_palindrome(test, expected):
    instance = StringMe(test)
    actual = instance.is_palindrome()
    assert expected == actual

@pytest.mark.parametrize("test, expected", [
    ("", True),
    ("(", False),
    (")", False),
    ("(()", False),
    ("(())", True)
])
def test_balanced(test, expected):
    instance = StringMe(test)
    actual = instance.is_balanced()
    assert expected == actual
