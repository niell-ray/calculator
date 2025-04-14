import art
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-': subtract,
    'x': multiply,
    '/': divide
}


def calculator():
    print(art.logo)
    continue_cal = True
    num1 = int(input("Enter the 1st number: \n"))
    while continue_cal:

        for keys in operations.keys():
            print(keys)
        operator = input("Enter operation: \n")

        num2 = int(input("Enter the 2nd number: \n"))

        print("\n")
        result = operations[operator](n1=num1, n2=num2)
        print(f"the result is: {result}\n\n")

        new_calculation = input(f"Type 'y' to continue with {result} or 'n' to start new: \n").lower()

        if new_calculation == 'y':
            num1 = result

        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()

