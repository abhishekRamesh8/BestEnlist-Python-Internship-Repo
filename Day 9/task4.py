# Write a Python program to find numbers divisible by 9 from a list of numbers

lst = list(range(1, int(input('Enter the length of list: ')) + 1))
print(list(filter(lambda x: (x % 9 == 0), lst)))
