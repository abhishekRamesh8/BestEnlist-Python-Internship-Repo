# Create a tuple and convert tuple into list

a = tuple(input('enter the value of tuple one at time: ') for i in range(int(input('enter the length of the tuple: '))))
print(a, f'type is {type(a)}')

# converting to tuple
print('after coversion')
a = list(a)
print(a, f'type is {type(a)}')