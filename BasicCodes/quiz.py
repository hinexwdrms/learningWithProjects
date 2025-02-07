#-----------------------------
def new_game():

    print("Welcome to the quiz! Try to answer the questions correctly!")

    qn_no = 1
    guesses = []
    your_score = 0

    for key in qn_ans:
        print("------------------------------------------------------------------------------")
        print(key)
        for i in options[qn_no - 1]:
            print(i)
        guess = input("Enter your answer (A B C OR D): ")
        guess = guess.upper()
        guesses.append(guess)

        your_score += check_results(qn_ans.get(key),guess)

        qn_no += 1

    scores(your_score,guesses)
#-----------------------------
def check_results(answers,guesses):
    if answers == guesses:
        print("Correct")
        return 1
    else:
        print("Incorrect")
        return 0

#-----------------------------
def scores(score,guesses):
    print("------------------------------------------------------------------------------")
    print("RESULTS")
    print("------------------------------------------------------------------------------")
    print("ANSWERS: ",end = "")
    for i in qn_ans:
        print(qn_ans.get(i), end=" ")
    print("")
    print("GUESSES: ",end="")
    for i in guesses:
        print(i,end=" ")
    print("")
    final_score = int((score/len(qn_ans))*100)
    print("Your total score is: "+ str(final_score) + "%")



#-----------------------------
def play_again():
    response = input("Do you want to play again? (y/n) : ")
    response = response.upper()
    if response == "Y":
        return True
    else:
        return False
#-----------------------------

qn_ans = {"Which planet is known as the Red Planet?":"B",
          "Who painted the famous artwork The Starry Night?":"B",
          "What is the chemical symbol for water?":"C",
          "Which of these is not a primary color in painting?":"C"}

options = [['A) Jupiter', 'B) Mars', 'C) Venus', 'D) Saturn'],
           ['A) Leonardo da Vinci', 'B) Vincent van Gogh', 'C) Pablo Picasso', 'D) Claude Monet'],
           ['A) W', 'B) Wa', 'C) H2O', 'D) Hy'],
           ['A) Red', 'B) Blue', 'C) Green', 'D) Yellow']]

new_game()

while play_again() == True:
    new_game()

print("Thank you for playing :)")

