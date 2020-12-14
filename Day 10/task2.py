# Write a Python program that matches a word containing 'ab'


import re

txt = input("enter a word: ")
ab = re.search('ab', txt)
if ab:
    print('starts at position {} and ends at position {}'.format(ab.span()[0], ab.span()[1]))

else:
    print('there is no word with \'ab\' in it')