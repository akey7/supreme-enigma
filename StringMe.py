from collections import deque

class StringMe:
    """
    These are various methods for doing operations on
    a string.

    Upon instanitation, you pass in a source string to
    a constructor. All the methods then pull from this
    string when they do their tests.
    """

    def __init__(self, source):
        self.source = source

    def is_palindrome(self, test_me=None):
        """
        Parameters
        ----------
        test_me : str
            Callers of this method should not use this
            parameters. This is used to pass shorter
            strings between recursive calls.

        Returns
        -------
        bool
            True if the string is a paindrome, false
            otherwise.
        """
        if test_me is None:
            test_me = self.source

        if len(test_me) < 2:
            return True
        elif test_me[0] != test_me[-1]:
            return False
        else:
            return self.is_palindrome(test_me[1:-1])

    def is_balanced(self):
        """
        Determiens if self.source has balened parenthesis

        Returns
        -------
        bool
            True of parens are balanced false otherwise.
        """
        stack = deque()
        for char in self.source:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    return False
        return len(stack) == 0

    def reflect(self):
        """
        Returns the source string

        Returns
        -------
            The source string
        """
        return self.source
