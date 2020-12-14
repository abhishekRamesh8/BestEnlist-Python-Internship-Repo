# Write a Python script to merge two Python dictionaries

import collections

pers = {'Name': 'R. Abhishek', 'ID': '21101'}
prof = {'lecture': 'Programming', 'Grade': 'A'}

res = collections.ChainMap(pers, prof)

if __name__ == '__main__':
    print(res.maps)

    print(f'keys = {list(res.keys())}')
    print(f'values = {list(res.values())}')
