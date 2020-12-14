# Write a Python program to match a string that contains only uppercase letters

import re

txt = input('Enter a string: ')

if re.fullmatch('[A-Z]+', txt):
    print('This string contains only uppercase')
else:
    print('Try another string')