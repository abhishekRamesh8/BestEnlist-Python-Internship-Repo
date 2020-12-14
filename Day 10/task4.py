# Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

import re

txt = input('Enter a string: ')

print(list(filter(lambda x: (3 >= len(x) > 0), re.findall('[0-9]+', txt))))

