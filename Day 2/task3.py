# Create two values (a,b) of int,float data type & convert the vise versa, Hint : convert a from int to float
# datatype & b from float to int datatype


# before swap
(a, b) = (2, 2.5)
print(f'{a=} and {b=}')

# after swap
(a, b) = (float(a), int(b))
print(f'{a=} and {b=}')
