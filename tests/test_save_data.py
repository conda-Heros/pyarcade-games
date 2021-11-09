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