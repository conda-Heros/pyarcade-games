"""
Quiz Game Tests
"""
from pyarcade_games.quiz_game import *

def test_display():
    msg="."
    actual=display(msg,"small")
    expected='   \n   \n _ \n(_)\n   \n'
    assert actual==expected
