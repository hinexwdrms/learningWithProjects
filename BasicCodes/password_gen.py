#password generator

import random
import string

print("Welcome to the password generator! ")

pass_length = int(input("Enter the password length: "))

pass_num = input("Would you like to include numbers? (y/n): ").lower()

if pass_num == "y":
    pass_num = True

pass_chars = input("Would you like to include special characters? (y/n): ").lower()

if pass_chars == "y":
    pass_chars = True


def generate_password(pass_length,pass_num,pass_chars):

    letters = string.ascii_letters
    numbers = string.digits
    characters = string.punctuation 
    combined_set = letters

    pwd = ""

    if pass_num == True:
        pwd += random.choice(numbers)               #atleast one number confirmed
        combined_set += numbers
    if pass_chars == True:
        pwd += random.choice(characters)            #atleast one character confirmed
        combined_set += characters                  


    for i in range(pass_length - len(pwd)):
        new_char = random.choice(combined_set)  
        pwd += new_char

    pass_list = list(pwd)
    random.shuffle(pass_list)
    final_pass = ''.join(pass_list)

    return final_pass

    #   CHECKING CRITERIA: (another way)
    #   if pass_num and not any(c.isdigit() for c in pwd):
    #       pwd = pwd[:-1] + random.choice(numbers)
    #   if pass_chars and not any(c in characters for c in pwd):
    #       pwd = pwd[:-1] + random.choice(characters)

print(generate_password(pass_length,pass_num,pass_chars))
