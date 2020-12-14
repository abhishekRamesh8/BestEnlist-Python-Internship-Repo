# Write a Python program that multiply each number of given list with a given number

lst = list(range(1, int(input('Enter the length of list: ')) + 1))
n = int(input('Enter the number to be multiply with: '))
print(list(map(lambda x: x * n, lst)))
