# Create a function getting two integer inputs from user. & print the following:
#
# Addition of two numbers is +value
# Subtraction of two numbers is +value
# Division of two numbers is +value
# Multiplication of two numbers is +value
#
# Here the value represents math function associated


def addition(a, b):
    print(f'Addition of two numbers is {a+b}\n')


def subtraction(a, b):
    print(f'Subtraction of two numbers is {a-b}\n')


def division(a, b):
    print(f'Division of two numbers is {a/b}\n')


def multiplication(a, b):
    print(f'Multiplication of two numbers is {a*b}')


num1, num2 = input("enter the num1 and num2 value separated by space \n").split()

addition(int(num1), int(num2))

subtraction(int(num1), int(num2))

division(int(num1), int(num2))

multiplication(int(num1), int(num2))
