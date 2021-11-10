from pyarcade_games.hangman import check_if_char_in_word, underscorify_word




def test_check_if_char_in_word():
    # Arrange
    expected = False
    # Actual
    actual = check_if_char_in_word("r","Mountain")
    # Expected
    assert actual == expected

def test_check_if_char_in_word_two():
    # Arrange
    expected = True
    # Actual
    actual = check_if_char_in_word("o","Global")
    # Expected
    assert actual == expected

def test_check_if_char_in_word_capital_letter():
    # Arrange
    expected = True
    # Actual
    actual = check_if_char_in_word("M","Mountain")
    # Expected
    assert actual == expected

def test_underscorify_word():
    # Arrange
    expected = "_____"
    # Actual
    actual = underscorify_word("store")
    # Expected
    assert actual == expected

def test_underscorify_word_with_num():
    # Arrange
    expected = "_____"
    # Actual
    actual = underscorify_word("store")
    # Expected
    assert actual == expected



def test_underscorify_word_with_num():
    # Arrange
    expected = None
    # Actual
    actual = underscorify_word("co5ol")
    # Expected
    print(actual)
    assert actual == expected