"""
Pylearn Game
"""
import time
import os
os.environ['DISPLAY'] = ':0'
from termcolor import cprint 
from pyfiglet import figlet_format
import tty
import sys
import termios
from pyarcade_games.save_data import save_data, retrive_value

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




    
def sense_user_input():
    """
    A function to sense the variation in the command line so that if the user press any key the user will be redirected to the next question
    """

    print("Press On any key to be directed to the questions.")

    orig_settings = termios.tcgetattr(sys.stdin)

    tty.setcbreak(sys.stdin)
    x = 0

    x=sys.stdin.read(1)[0]


    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
    return None

def lessons_and_questions_mode1():
    """
    This function contain the whole lessons for mode1 for this game and all of the questions and the answers
    
    arguments=>None
    Return=>list
    """
    lessons_questions_answers=[

    {'lesson0':'Lesson 1: Programming is the process of creating a set of instructions that tell a computer how to perform a task. Programming can be done using a variety of computer programming languages, such as JavaScript, Python, and C++',
    'question0':"""Python is a:
    A- Development environment

    B- Set of editing Tools

    C- Programming Language""",
    'answer0':'C'},


    {'lesson1':'Lesson 2: Let\'s start off by creating a short program that displays (Hi!).In Python, we use the print statement to output text. ',
    'question1':"""Select the correct option to output "Hi".
    A- count('Hi')

    B- cprint('Hi')

    C- print('hi')
    
    D- print('Hi')""",
    'answer1':'D'} ,
    
    {'lesson2':'Some characters can\'t be directly included in a string which is the text between two single or double quotation marks. For instance, double quotes can\'t be directly included in a double quote string; this would cause it to end prematurely.Characters like these must be escaped by placing a backslash before them.Double quotes only need to be escaped in double quote strings, and the same is true for single quote strings. ',

    'question2':"""Which of the following command will output a string containing single quote.
    A- print('Just say "Good morning"')

    B- print('I'm learning!')

    C- print('I\\'m learning!')
    
    D- print('Welcome to programming world!')""",
    'answer2':'C'},

    {'lesson3':"""A variable allows you to store a value by assigning it to a name, which can be used to refer to the value later in the program.To assign a variable, use one equals sign : Example(user = "James"  )
    Certain restrictions apply in regard to the characters that may be used in Python variable names. The only characters that are allowed are letters, numbers, and underscores. Also, they can\'t start with numbers.Not following these rules results in errors. """,

    'question3':"""Which of these is a valid variable name in Python?

    A- a-variable-name

    B- A_VARIABLE_NAME

    C- a variable name
    
    D- a.variable.name""",
    'answer3':'B'},
    {'lesson4':"""To get input from the user in Python, you can use the intuitively named input function.
For example, a game can ask for the user's name and age as input and use them in the game.

The input function prompts the user for input, and returns what they enter as a string (with the contents automatically escaped).The input statement needs to be followed by parentheses.""",

    'question4':"""What is the type of 'X' reagrding the following command:
    X=input('How old are you?')


    A- string

    B- boolean 

    C- integer
    
    D- Float""",
    'answer4':'A'}]
    return(lessons_questions_answers)



def start_lessons_and_questions(lessons_and_questions_mode1):
    
    lessons_questions_info=lessons_and_questions_mode1()

    total_marks=0


    for num in range(len(lessons_questions_info)):
        os.system('clear')
        # print instructor picture
        print(welcoming_picture_to_game())
        # print lessons
        print(lessons_questions_info[num][f'lesson{num}'])
        print('')
        sense_user_input()
        #starts calculating time from the following line
        os.system('clear')
        start = time.time()
        print(lessons_questions_info[num][f'question{num}'])
        user_answer=input('> Answer: ')
        # check for the time that the user took to answer
        
        while (time.time() - start) > 10:
            os.system('clear')
            # playsound('voicenote.mp3')
            print("""Are you sure ?
            A - Yes
            B -No
            """)
            user_confirmation=input('> Answer:')
            while user_confirmation.upper() != 'YES' and user_confirmation.upper() != 'NO':
                print('Its a Yes or No question , Just answer with one of Them !')
                user_confirmation=input('> Answer:')
            if user_confirmation.upper() == 'YES':
                break
            else:
                start = time.time()
                print(lessons_questions_info[num][f'question{num}'])
                user_answer=input('> Answer: ')
                



        if user_answer.upper()==lessons_questions_info[num][f'answer{num}']:
            total_marks+=20
        else:
            pass
    existing_score = retrive_value("pylearn_score")
    if existing_score and existing_score > total_marks:
        pass
    else:
        save_data("pylearn_score",total_marks)
    return cprint(figlet_format(f'Your Total marks is : {total_marks}  Out of 100', font='doom'),
    'white', 'on_blue', attrs=['bold'])


def before_user_start_game():
    print('To start this game just Type in \'Go\' !')
    user_select=input('> ')
    while(user_select.upper() != 'GO'):
        print('please type in \'Go\' to start !')
        user_select=input('> ')
    os.system('clear')
    return ''
    






def main():
    print(welcoming_picture_to_game())
    print(welcoming_text_to_game())
    print(before_user_start_game())
    print(start_lessons_and_questions(lessons_and_questions_mode1))
