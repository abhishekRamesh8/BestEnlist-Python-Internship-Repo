# •	Create a calculator only on a code level by using if condition (Basic arithmetic calculation)

num1 = float((input('Enter number one: ')))
num2 = float(input('Enter number two: '))

op = int(input("""enter any one of the following operation: 
                1. addition
                2. subtraction
                3. multiply
                4. divide
                """))

print('The answer is', end=' ')
if op == 1:
    print(num1 + num2)

elif op == 2:
    print(num1 - num2)

elif op == 3:
    print(num1 * num2)

elif op == 4:
    print(num1 / num2)

else:
    print('try again with correct input')