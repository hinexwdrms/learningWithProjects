import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

play = input("Do you want to start? (yes/no) : ").lower()

if play == "no":
    quit()

if play != "yes":
    print("only YES or NO !")

print("-------------------------------")
numbers = list(range(1,101))
correct_ans = random.choice(numbers)
tries = 0

    #difficulty level
difficulty_map = {
    "1": ("Easy", 10),
    "easy": ("Easy", 10),
    "2": ("Medium", 5),
    "medium": ("Medium", 5),
    "3": ("Hard", 3),
    "hard": ("Hard", 3)
    }

difficulty = input("Enter your choice (1/Easy, 2/Medium, 3/Hard): ").lower()

difficulty_details = difficulty_map.get(difficulty)

if difficulty_details:
    level_name, chances = difficulty_details
    print(f"Great! You have selected '{level_name}' difficulty. You have {chances} chances.")
else:
    print("Invalid choice! Please restart and select a valid difficulty level.")
    exit()

    #game loop
for i in range(chances):

    tries += 1
        
    guess = int(input("Guess the number (You have "+ str(chances - tries) + " tries left): "))

    if guess == correct_ans:
        print("You win! the number was: "+ str(correct_ans))
        print("Congratulations! It took you "+str(tries)+" tries!")
        break
        
    elif tries == chances:
        print(f"You could not guess the number!\nThe number was {correct_ans}\n-----YOU LOSE-----")

    else:
        if guess > correct_ans:
            symbol = "less"
        elif guess < correct_ans:
            symbol = "greater"

        print(f"The number is {symbol} than {guess}")            

        

