# Write a Python program to create Fibonacci series to n using Lambda


def fibonacci(count):
    lst = [0, 1]

    any(map(lambda _: lst.append(sum(lst[-2:])),
            range(2, count)))

    return lst[:count]


print(fibonacci(int(input("Enter n to list the Fibonacci series up to it: "))))
