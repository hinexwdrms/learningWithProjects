import random

print("Welcome to the game!")

while True:

    choices = ["rock","paper","scissors"]

    computer_ans = random.choice(choices)

    player_ans = None
    while player_ans not in choices:
        player_ans = input("rock, paper or scissors: ").lower()

    print("Your Answer: {}".format(player_ans))
    print("Computer's Answer: {} ".format(computer_ans))

    #score = 0 add scores!
    #ties = 0
    #comp_score = 0

    if player_ans == computer_ans:
        print("Tie!")
    elif player_ans == "rock" and computer_ans == "scissors":
        print("You win!!")
    elif player_ans == "paper" and computer_ans == "rock":
        print("You win!")
    elif player_ans == "scissors" and computer_ans == "paper":
        print("You Win!")
    else:
        print("Computer Wins!")

    yes_no = ["Y","N"]

    still_play = None
    while still_play not in yes_no:
        still_play = input("Would you still like to play? (Y/N) :").upper()

    if still_play != "Y":
        break
print("BYE!")