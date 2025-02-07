import time
import random

print("Welcome to the timed math challenge! \nSolve the challenge as quick as you can!")
total_problems = int(input("How many problems would you like to face? : "))

operators = ["+","-","*"]
max_val = 12
min_val = 3

def generate_problem():
    left = random.randint(min_val,max_val)
    right = random.randint(min_val,max_val)
    operand = random.choice(operators)

    problem = str(left) + " " + str(operand) + " " + str(right)
    ans = eval(problem)
    
    return problem,ans

input("Press ENTER to start")
min_time = time.time()
score = 0

for i in range(total_problems):
    problem,ans = generate_problem()
    user_ans = input("#PROBLEM"+" "+str((i+1))+": " + str(problem)+"= ")
    if int(user_ans) == ans:
        score += 1

max_time = time.time()

print("----------------------------------------------------")
print("Congratulations! You scored "+ str(score) + " out of " + str(total_problems))
time_taken = max_time - min_time
print("You took: "+str(int(time_taken))+" seconds!")


    




