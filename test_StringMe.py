from StringMe import StringMe

def test_reflect():
    expected = "hello"
    instance = StringMe(expected)
    actual = instance.reflect()
    assert expected == actual
        
def test_palindrome():
    instance = StringMe("")
    expected = True
    actual = instance.isPalindrome()
    assert expected == actual
