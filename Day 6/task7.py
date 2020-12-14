# •	Write a program to convert the number of days to ages

import datetime


date = input("enter date in the format YYYY-MM-DD: ")
day = (datetime.datetime.now() - datetime.datetime.fromisoformat(date)).days
print(f'The number of days are {day} and age is {day//365}')

