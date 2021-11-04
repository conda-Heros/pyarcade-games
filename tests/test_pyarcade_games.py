from pyarcade_games import __version__
from main import say_hi

def test_version():
    assert __version__ == '0.1.0'



def test_say_hi():
    # Arrange
    expected = "Hi"
    # Actual
    actual = say_hi()
    # Assert
    assert actual == expected