"""
Main Game Module
"""
from colorama import Fore, Style
from PyInquirer.prompt import prompt
import pyfiglet
import sys
import os



def start_application():
    """
    Application Start Method
    """
    start_message = Fore.CYAN + Style.BRIGHT + pyfiglet.figlet_format("PyArcade Games")
    print(start_message)
    question = [
        {
            "type": "list",
            "name": "game",
            "message": "Choose A Game To Play.",
            "choices": [
                "Hang Man",
                "Quiz Game",
                "Snake",
                "Pylearn",
                "View Scores",
                "Quit"
            ],
        }
    ]
    
    # play Game Video
    os.system('video-to-ascii -f dancing_man.mp4 --strategy filled-ascii')

    answer = prompt(question).get("game")
    if answer == "Hang Man":
        from pyarcade_games.hangman import start_hangman_game
        start_hangman_game()
    elif answer == "Quiz Game":
        from pyarcade_games.quiz_game import main
        main()
    elif answer == "Snake":
        from pyarcade_games.snake_game import main
        main()
    elif answer == "Pylearn":
        from pyarcade_games.pylearn import main
        main()
    elif answer == "View Scores":
        from pyarcade_games.scores_menu import view_scores
        view_scores()
    elif answer == "Quit":
        quit_game()
        

def quit_game():
    print(f"{Fore.RED} Quiting Game....")
    sys.exit()



if __name__ == "__main__":
    start_application()