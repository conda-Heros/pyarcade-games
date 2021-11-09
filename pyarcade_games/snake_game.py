import curses
from random import randint
import random
from colorama import Fore,  Style
import pyfiglet



def main():
    curses.initscr()
    curses.start_color()
    win = curses.newwin(25 , 80 , 2, 20)
    win.keypad(1)

    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    curses.start_color()
    # Snake and Food :
    snake = [(4, 10) , (4 , 9) , (4,8)]
    food=(10,20)
    # game logic :

    score= 0
    Highest_Score = 0


    ESC = 27
    key = curses.KEY_RIGHT

    food_ch = ('🍕' , '🍔' , '🍩' , '🍉' ,'🍎' )
    foodch =random.choice(food_ch)

    while key != ESC:
        win.addstr(0 , 70 ,   " Score " + str(score) +' ' ) 
        # win.addstr(0 , 80 ," Highest_Score " + str(Highest_Score) +' ' ) 
        win.addstr(0 , 1 ,'🐍' ) 
        win.timeout(150 - (len(snake)) //5 + len(snake)//10 % 120)

       

        prev_key = key

        event = win.getch()
        key= event if event != -1 else prev_key



        # calculate the next coordinate 

        y = snake[0][0]
        x = snake[0][1]

        if key == curses.KEY_DOWN:
            y+=1

        elif key == curses.KEY_UP:
            y-=1    

        elif key == curses.KEY_RIGHT:
            x+=1
        
        elif key == curses.KEY_LEFT:
            x-=1

        else:
            
         if key not in [curses.KEY_RIGHT , curses.KEY_LEFT , curses.KEY_UP , curses.KEY_DOWN , ESC]:
            key = prev_key


        snake.insert(0 , (y ,x))

        # check if the snake hit the border

        if y == 0 : break
        if y== 24 : break
        if x == 0 :break
        if x== 79 :break


        # check if the snake runs oner itself :
        if snake[0] in snake[1:] : break


        # check if the snake eat the food :

        if snake[0] == food :
            score+=1
            if Highest_Score <= score :
             Highest_Score=score
            
            food=()
            foodch =random.choice(food_ch)

            while food == ():
                # get a random coordinate for the food
                food = (randint(1,23) , randint(1,78))

                # check that the random coordinate not on the snake coordinate
                if food in snake :
                    food =()

            win.addch(food[0] , food[1] , foodch)

        else :
            # move the snake to delete the current coordinate 
            last = snake.pop()
            win.addch(last[0] , last[1] , ' ')

        win.addch(snake[0][0] , snake[0][1] , '☀' )               

        

        for c in snake :
            win.addch(c[0] , c[1] , '☀')

        win.addch(food[0] , food[1] ,foodch)


    curses.endwin()
    Lose_meassage = Fore.RED+ Style.BRIGHT + pyfiglet.figlet_format("You Lose ")

    score_meassage = Fore.BLUE+ Style.BRIGHT + pyfiglet.figlet_format(f"Score : {score} ")
    print(Lose_meassage)
    print( score_meassage)
    user_input = input('Try again ?')
    if user_input == 'yes' or user_input=='y':
        from hangman import clear_console
        clear_console()
        main()
        
     





# print(Style.BRIGHT + f"Highest_Score : {Highest_Score} ")

if __name__ == "__main__":
    main()