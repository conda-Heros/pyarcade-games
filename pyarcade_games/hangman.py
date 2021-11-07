"""
Hangman Game Module

"""
from colorama import Fore, Style
import random
import pyfiglet
import os
default_tries = 6
hangman_states = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]
words_bank = []
with open("assets/hangman_words.txt") as file:
    words_bank = file.readlines()

def start_hangman_game(tries=default_tries, word=words_bank[random.randint(0,len(words_bank)-1)]):

    clear_console()
    start_message = Fore.RED + Style.BRIGHT + pyfiglet.figlet_format("Hangman")
    print(start_message)
    print(Fore.GREEN + "Game Rules: ")

    print(f"1: You have {tries} tries to guess the correct letters of a randomized word")
    print(f"2: If you input a correct letter, the Hangman will stay in his current state without losing any of the tries you have.")
    print(f"3: If you input a wrong letter, then the hangman state will update and you will lose 1 try ")

    
    while tries >= 1:
        modified_word = ""
        for i in word:
            modified_word+= " _"
        print(Fore.WHITE + hangman_states[tries])
        print(modified_word)
        user_input = input("Take a guess: ")


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


if __name__ == "__main__":
    start_hangman_game()
