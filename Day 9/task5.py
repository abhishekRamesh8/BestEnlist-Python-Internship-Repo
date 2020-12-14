# Write a Python program to count the even numbers in a given list of integers

lst = list(range(1, int(input('Enter the length of list: ')) + 1))
print(list(map(lambda x: (x % 2 == 0), lst)).count(True))
