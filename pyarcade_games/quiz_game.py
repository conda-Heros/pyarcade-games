from pyfiglet import Figlet
import readchar
import sys

def display(msg,style):
    """
    Display function for ASCII art text generation 

    Arg: 
        msg: string argument for the messege to be printed
        style: special argument to select the style of messge to be printed
    Return:
        result : a messege in ASCII art style
    """
    f = Figlet(font=style)
    result=f.renderText(msg)
    print(result)
    return result

def main():
    """
    Main function for Runinng the game

    Arg: 
        No Argument
    Return:
        No return Value
    """ 
    display("     Covid-19 Quiz Game","small")	
    print('Enter s to start the game, q to exit : ')
    char=readchar.readchar()
    if char== 's':
        # ------------------------- Play ------------------------------
        display("     Quiz Game","small")
        print("Welcome to the quiz game, we have 10 questions to answer and you will get your score at the end, Good Luck!")
    else:
        main()
