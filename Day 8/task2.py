print("===WELCOME TO MY CALCULATOR===")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice = int(input("Please choose what operation you wanna do : "))

a = int(input("Please give me first number : "))
b = int(input("Please give me second number : "))

if (choice == 1):
    try:
        if (type(a), type(b) == int):
            print(a + b)
    except TypeError:
        print("your input is not number")
elif (choice == 2):
    try:
        if (type(a), type(b) == int):
            print(a - b)
    except TypeError:
        print("your input is not number")
elif (choice == 3):
    try:
        if (type(a), type(b) == int):
            print(a * b)
    except TypeError:
        print("your input is not number")
elif (choice == 4):
    try:
        if (type(a), type(b) == int):
            if (b != 0):
                print(a / b)
            else:
                print("your second number is less than 1")
    except TypeError:
        print("your input is not number")
else:
    print("you give us invalid choice")
