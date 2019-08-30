class StringMe:
    def __init__(self, source):
        self.source = source

    def is_palindrome(self, test_me=None):
        if test_me is None:
            test_me = self.source

        if len(test_me) < 2:
            return True
        elif test_me[0] != test_me[-1]:
            return False
        else:
            return self.is_palindrome(test_me[1:-1])

    def isBalanced(self):
        pass

    def reflect(self):
        return self.source
