# Create a tuple and print the reverse of the created tuple

tup = tuple(input('enter the value of tuple one at time: ') for i in range(int(input('enter the length of the tuple: '))))
print(tuple(list(tup).__reversed__()))