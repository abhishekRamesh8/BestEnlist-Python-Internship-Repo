# .	Write a program to create a list of n integer values and do the following
# •	Add an item in to the list (using function)
# •	Delete (using function)
# •	Store the largest number from the list to a variable
# •	Store the Smallest number from the list to a variable


list1 = [int(input(f'enter {i} value of the list: ')) for i in range(1, int(input('enter the length of list: ')) + 1)]

# •	Add an item in to the list (using function)
list1.append(int(input('enter the item to add: ')))
print(list1)

# •	Delete (using function)
list1.remove(int(input('enter the item to delete: ')))
print(list1)

# •	Store the largest number from the list to a variable
print(f'the largest number in the list is {max(*list1)}')

# •	Store the Smallest number from the list to a variable
print(f'the smallest number in the list is {min(*list1)}')
