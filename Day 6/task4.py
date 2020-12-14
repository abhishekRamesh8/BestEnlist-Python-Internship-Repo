# •	Explain Armstrong number and write a code with a function

"""If the given number is equal to the sum of the Nth power of each digit present in that integer, then that number
    can be an Armstrong Number in Python. For example, 370 is Armstrong Number"""


def armstrong(num, count=0):
    n = list(map(int, str(num)))
    p = len(n)
    for i in range(p):
        count = count + pow(n[i], p)
    if str(count) == num:
        print('Armstrong number')
    else:
        print('Not an Armstrong number')


armstrong(input("Enter a number: "))
