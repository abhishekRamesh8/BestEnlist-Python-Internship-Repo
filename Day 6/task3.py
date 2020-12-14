# •	Python Program to Print the Fibonacci sequence

def fibonacci(num):
    a = 0
    b = 1
    for i in range(0, num):
        a = a + b
        b = a - b
        print(a)


fibonacci(int(input()))
