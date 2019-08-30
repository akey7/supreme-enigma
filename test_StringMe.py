import pytest
from StringMe import StringMe

def test_reflect():
    expected = "hello"
    instance = StringMe(expected)
    actual = instance.reflect()
    assert expected == actual
        
@pytest.mark.parametrize('test, expected', [("", True)])
def test_palindrome(test, expected):
    instance = StringMe(test)
    actual = instance.isPalindrome()
    assert expected == actual
