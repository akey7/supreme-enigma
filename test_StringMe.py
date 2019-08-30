from StringMe import StringMe

class TestStringMe():
    def test_reflect(self):
        expected = "hello"
        instance = StringMe(expected)
        actual = instance.reflect()
        assert expected == actual
        
