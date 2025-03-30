#building a airthmetic formatter
#imp: no need to do if: else: in function if we just return the function ends.
def arithmetic_arranger(problems, show_ans=False):
    # Checking the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initializing lines
    first_line = ''
    second_line = ''
    third_line = ''
    result_line = ''

    for i, problem in enumerate(problems):
        list_of_terms = problem.split()
        first_term = list_of_terms[0]
        operator = list_of_terms[1]
        second_term = list_of_terms[2]

        # Check conditions
        check = check_conditions(first_term, second_term, operator)
        if check is not True:
            return check  # Return the error message

        # Find the width of the problem
        width = max(len(first_term), len(second_term)) + 2  # Adjust width for spacing

        # Build each line of the formatted output
        first_line += f'{first_term:>{width}}'
        second_line += f'{operator} {second_term:>{width - 2}}'
        third_line += f'{"-" * width}'

        if show_ans:
            if operator == '+':
                result = str(int(first_term) + int(second_term))
            else:
                result = str(int(first_term) - int(second_term))
            result_line += f'{result:>{width}}'

        # Add four spaces between problems **except for the last problem**
        if i < len(problems) - 1: #len returns no. of terms while i is one index less
            first_line += "    "
            second_line += "    "
            third_line += "    "
            if show_ans:
                result_line += "    "

    # Return the properly formatted string
    if show_ans:
        return f"{first_line}\n{second_line}\n{third_line}\n{result_line}"
    else:
        return f"{first_line}\n{second_line}\n{third_line}"


def check_conditions(first_term, second_term, operator):
    if operator not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
    if not first_term.isdigit() or not second_term.isdigit():
        return "Error: Numbers must only contain digits."
    if len(first_term) > 4 or len(second_term) > 4:
        return "Error: Numbers cannot be more than four digits."
    return True


# Test the function
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
