# TYPE ERROR
try:
    a = '1'
    print(a - a)
except TypeError:
    print("Type Error!!")

# ARITHMETIC ERROR
try:
    a = 1
    b = 0
    print(a / b)
except ArithmeticError:
    print("Division by Zero!!")

# INDEX ERROR
try:
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a[10])
except IndexError:
    print("List index out of bound!!")

# VALUE ERROR
try:
    a = int(input("please give me the password : "))
except ValueError:
    print("Password Must be the number!!")

# IMPORT ERROR
try:
    from math import sq
except ImportError:
    print("could not import sq!!")

# NAME ERROR
try:
    a = 50
    print(b)
except NameError:
    print("Variable is not defined")
