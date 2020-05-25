
def addition():
    """take two user numbers and add them"""

    prompt1 = "What's the first number you want to add?"
    num_1 = return_if_int(prompt1)
    prompt2 = "What's the second number you want to add?"
    num_2 = return_if_int(prompt2)

    sum = num_1+num_2
    return sum


def return_if_int(prompt):
    """takes user input number and returns the number if
    it's an integer"""
    try:
        num = int(input(prompt))
    except ValueError:
        print("Sorry, that's not a number!")
        num = return_if_int(prompt)
        return num
    else:
        return num


print(addition())
