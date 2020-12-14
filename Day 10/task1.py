# Write a Python program for all the cases which can check a string contains only a certain set of characters (in
# this case a-z, A-Z and 0-9).


import re

string = input('Enter a string: ')

if re.fullmatch('[A-Z]+', string):
    print('String only contains only uppercase letters(A-Z)')

elif re.fullmatch('[a-z]+', string):
    print('String only contains only lowercase letters(a-z)')

elif re.fullmatch('[0-9]+', string):
    print('String only contains only digits(0-9)')

else:
    print('Try again')
