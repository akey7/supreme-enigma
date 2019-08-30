class StringMe:
    def __init__(self, source):
        self.source = source

    def isPalindrome(self, test_me=None):
        if test_me is None:
            test_me = self.source

        if len(test_me) < 2:
            return True
        elif test_me[0] != test_me[-1]:
            return False
        else:
            return self.isPalindrome(test_me[1:-1])

    def reflect(self):
        return self.source
