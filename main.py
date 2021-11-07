"""
Main Game Module
"""
from colorama import Fore, Style
from PyInquirer import prompt
import pyfiglet


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

    answer = prompt(question).get("game")


if __name__ == "__main__":
    start_application()