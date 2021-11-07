from pyarcade_games.pylearn import *
def test_welcoming_picture_to_game():

    # arrange
    with open('pic.txt',mode='r') as file:
        content=file.read()
    expected=content
    # act
    ASCI_art_pic=welcoming_picture_to_game()
    actual=ASCI_art_pic
    #assert
    assert actual == expected

def test_welcoming_to_game():
    # arrange
    

    introduction="""                                                  Welcome to Pylearn !
                                I am Dario Thornhill and i will be your instructor in this Game !
                                i will help you to learn programming in a very Easy and nice way !
                                            lets get started"""
    expected=introduction
    # act
    Greeting=welcoming_text_to_game()
    actual=Greeting
    #assert
    assert actual == Greeting

def test_lessons_and_questions_mode1():
    # act
    actual=len(lessons_and_questions_mode1())
    expected=5
    # assert
    assert actual==expected

def test_start_lessons_and_questions():
    pass


