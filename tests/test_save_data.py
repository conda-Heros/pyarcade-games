from pyarcade_games.save_data import save_data





def test_save_data():
    # Arrange
    save_data("dummy_variable", 5)
    expected = 5
    # Actual
    actual = None
    try:
        import games_data.saves as saves
        actual = saves.dummy_variable
    except:
        pass
    # Assert
    assert actual == expected



def test_save_data_stromg():
    # Arrange
    save_data("dummy_string_variable", "I am a lovely string")
    expected = "I am a lovely string"
    # Actual
    actual = None
    try:
        import games_data.saves as saves
        actual = saves.dummy_string_variable
    except:
        pass
    # Assert
    assert actual == expected