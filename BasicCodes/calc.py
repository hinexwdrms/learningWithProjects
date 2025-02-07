#calculator

print("\nWelcome to the calculator!\n")
start = input("Would you like to start?: (Y/N): ").upper()

if start == "Y":
    var1 = int(input("Enter the first number: "))
    var2 = int(input("Enter the second number: "))
    operator = str(input("Enter the operation ('+','-','*','/'): "))

    if operator == "+":
        result = var1 + var2

    elif operator == "-":
        result = var1 - var2
        
    elif operator == "*":
        result = var1 * var2

    elif operator == "/":
        result = float(var1 / var2)

    print("Your result is : "+ str(result))

elif start != "N":
    print("Please enter a valid option!")



