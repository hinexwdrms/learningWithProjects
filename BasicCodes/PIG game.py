#fix errors

import random


p1_score = 0
p2_score = 0

def play_game_p1():
    global p1_score

    print("----------------Player 1's TURN-----------------")
    input("press ENTER to start rolling dice: ")

    roll_p1 = True
    p1_win = None

    while roll_p1:

        dice_output = random.randint(1,6)
        p1_score += dice_output

        print("You rolled a: "+ str(dice_output))
        
        if dice_output == 1:
            p1_win == False
            print("Your Turn is over. You rolled a 1 !")
            break

        if p1_score >= 50:
            p1_win == True
            print("Congratulations you reached 50 points! ")
            break
            
        play_again = input("Your score is now: " +str(p1_score)+
                           " \n--------(Y/N) ROLL AGAIN?--------  : ").lower()
        
        if play_again =="n":
            roll_p1 = False

    return p1_win,p1_score

def play_game_p2():
    global p2_score

    print("----------------Player 2's TURN-----------------")
    input("press ENTER to start rolling dice: ")

    roll_p2 = True
    p2_win = None

    while roll_p2:

        dice_output = random.randint(1,6)
        p2_score += dice_output

        print("You rolled a: "+ str(dice_output))
        
        if dice_output == 1:
            p2_win = False
            print("Your Turn is over. You rolled a 1 !")
            break

        if p2_score >= 50:
            p2_win = True
            print("Congratulations you reached 50 points! ")
            break

        play_again = input("Your score is now: " +str(p2_score)+
                           " \n--------(Y/N) ROLL AGAIN?--------  : ").lower()
        
        if play_again =="n":
            roll_p2 = False

    return p2_win,p2_score

print("-----------WELCOME------------------")
print("LETS START! FIRST TO GET 50 POINTS WIN! ")
input("PRESS ANY KEY TO BEGIN!")

p1_win = False
p2_win = False

while not (p1_win or p2_win):
    p1_win, p1_score = play_game_p1()
    if p1_win:
        break
    p2_win, p2_score = play_game_p2()
    if p2_win:
        break

if p1_win:
    print("Player 1 won!")
    print("Player 2 had", p2_score, "score! So close.")
else:
    print("Player 2 won!")
    print("Player 1 had", p1_score, "score! So close.")