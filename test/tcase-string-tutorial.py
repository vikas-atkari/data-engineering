import pytest


class TestStringTutorial:
    """Test cases for string operations"""
    
    def test_string_concatenation(self):
        """Test string concatenation"""
        str1 = "Hello"
        str2 = "World"
        result = str1 + " " + str2
        assert result == "Hello World"
    
    def test_string_length(self):
        """Test string length"""
        test_string = "Python"
        assert len(test_string) == 6
    
    def test_string_upper(self):
        """Test converting string to uppercase"""
        test_string = "hello"
        assert test_string.upper() == "HELLO"
    
    def test_string_lower(self):
        """Test converting string to lowercase"""
        test_string = "HELLO"
        assert test_string.lower() == "hello"
    
    def test_string_split(self):
        """Test string splitting"""
        test_string = "Hello,World,Python"
        result = test_string.split(",")
        assert result == ["Hello", "World", "Python"]
    
    def test_string_replace(self):
        """Test string replacement"""
        test_string = "Hello World"
        result = test_string.replace("World", "Python")
        assert result == "Hello Python"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])