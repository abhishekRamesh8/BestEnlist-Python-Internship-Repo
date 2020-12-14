"""To write a program to get the below pattern
        54321
        4321
        321
        21
        1"""

a = '54321'
for i in range(len(a), 0, -1):
    print(a[-i:])
