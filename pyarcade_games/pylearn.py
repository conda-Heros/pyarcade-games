"""
Pylearn Game
"""
import time
import os
from termcolor import cprint 

from pyfiglet import figlet_format


def countdown(t):

    """A function to count the time remained for the lesson to end and to start the question
    Argument=>None
    Return=>string"""
    
    
    while t:
        # divide time to minitues and second
        mins, secs = divmod(t, 60)
        # update timer 
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        # delay for 1 second
        time.sleep(1)
        t -= 1
      
    print('You are Out of Time!')
  
  


  


def welcoming_picture_to_game():
    """
    Function to display the image of the instructor in ASCI art
    arguments=>None
    Return=>string
    """
    # loading the picture of instructor in ASCI ART
    with open('pic.txt',mode='r') as file:
        content=file.read()
    return(content)

def welcoming_text_to_game():
    """
    Function to display the introduction about the instructor
    arguments=>None
    Return=>string
    """
    introduction="""                                                  Welcome to Pylearn !
                                I am Dario Thornhill and i will be your instructor in this Game !
                                i will help you to learn programming in a very Easy and nice way !
                                                lets get started"""
    return(introduction)

    




def main():
    print(welcoming_picture_to_game())
    print(welcoming_text_to_game())
