"""
Quiz Game Tests
"""
from pyarcade_games.quiz_game import *

def test_display():
    msg="."
    actual=display(msg,"small")
    expected='   \n   \n _ \n(_)\n   \n'
    assert actual==expected

def test_get_score_happy_path():
    user_answers ={'howPass': 'Through droplets that come from your mouth and nose when you cough or breathe out', 'isPositve': 'No – not everyone with COVID-19 has symptoms', 'symptoms': 'All of the above', 'HIV': 'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk', 'peopleInDanger': 'Older people – especially those aged 70 and above', 'isCured': 'No – but most people get better by themselves', 'isProtect': 'Yes – normal soap and water or hand sanitizer is enough', 'protectHIV': 'All of the above', 'maskWorn': 'All of the above', 'distance': 'You stop going to crowded places and visiting other people’s houses'}
    user_answers = [j for j in user_answers.values()]
    correct_answers = [
        'Through droplets that come from your mouth and nose when you cough or breathe out',
        'No – not everyone with COVID-19 has symptoms',
        'All of the above',
        'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk',
        'Older people – especially those aged 70 and above',
        'No – but most people get better by themselves',
        'Yes – normal soap and water or hand sanitizer is enough',
        'All of the above',
        'All of the above',
        'You stop going to crowded places and visiting other people’s houses',]
    actual=get_score(correct_answers,user_answers)
    expected=10
    assert actual==expected

def test_get_score_normal_path():
    user_answers={'howPass': 'In sexual fluids, including semen, vaginal fluids or anal mucous', 'isPositve': 'No – not everyone with COVID-19 has symptoms', 'symptoms': 'All of the above', 'HIV': 'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk', 'peopleInDanger': 'Older people – especially those aged 70 and above', 'isCured': 'Yes – Hot drinks can cure COVID-19', 'isProtect': 'No – Washing your hands doesn’t stop COVID-19', 'protectHIV': 'Exercise regularly, eat well and look after their mental health', 'maskWorn': 'In small shops', 'distance': 'You stop talking to the people you live with'}
    user_answers = [j for j in user_answers.values()]
    correct_answers = [
        'Through droplets that come from your mouth and nose when you cough or breathe out',
        'No – not everyone with COVID-19 has symptoms',
        'All of the above',
        'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk',
        'Older people – especially those aged 70 and above',
        'No – but most people get better by themselves',
        'Yes – normal soap and water or hand sanitizer is enough',
        'All of the above',
        'All of the above',
        'You stop going to crowded places and visiting other people’s houses',]
    actual=get_score(correct_answers,user_answers)
    expected=4
    assert actual==expected
    
def test_get_score_sad_path():
    user_answers ={}
    user_answers = [j for j in user_answers.values()]
    correct_answers = [
        'Through droplets that come from your mouth and nose when you cough or breathe out',
        'No – not everyone with COVID-19 has symptoms',
        'All of the above',
        'No – people who adhere to antiretroviral treatment (ART) and have a high CD4 count aren’t more at risk',
        'Older people – especially those aged 70 and above',
        'No – but most people get better by themselves',
        'Yes – normal soap and water or hand sanitizer is enough',
        'All of the above',
        'All of the above',
        'You stop going to crowded places and visiting other people’s houses',]
    actual=get_score(correct_answers,user_answers)
    expected=0
    assert actual==expected