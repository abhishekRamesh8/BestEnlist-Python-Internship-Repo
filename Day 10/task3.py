# Write a Python program to check for a number at the end of a word/sentence

import re

txt = input('Enter a sentence or a word: ')

if re.search('\d$', txt):
    print('number exists')