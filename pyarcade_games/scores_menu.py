"""
View Game Scores Module
"""
from pyarcade_games.hangman import clear_console
from colorama import Fore, Style
from pyarcade_games.save_data import retrive_value
import pyfiglet

def view_scores():
    """
    A function that gets all scores of the pyarcade games and displays them in one place.

    Args:
        None
    Returns:
        None
    """
    clear_console()
    scores_message = Fore.CYAN + Style.BRIGHT + pyfiglet.figlet_format("Scores")
    print(scores_message)
    hangman_score = retrive_value("hangman_score")
    quizgame_score = retrive_value("quizgame_score")
    snake_score = retrive_value("snake_score")
    pylearn_score = retrive_value("pylearn_score")
    print(f"{Fore.RESET}Hangman: {Fore.BLUE}{hangman_score}")
    print(f"{Fore.RESET}Quiz Game: {Fore.BLUE}{quizgame_score}")
    print(f"{Fore.RESET}Snake Game: {Fore.BLUE}{snake_score}")
    print(f"{Fore.RESET}PyLearn Game: {Fore.BLUE}{pylearn_score}")

    print(f"{Fore.CYAN}Press any key to go back to the main menu.")
    


if __name__ == "__main__":
    view_scores()