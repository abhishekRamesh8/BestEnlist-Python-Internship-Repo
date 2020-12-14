# 	Try getting an input inside the try catch block

try:
    print('Enter only integer values')
    while True:
        int(input('enter space( ) to break the loop: '))

except ValueError:
    print("You ended the loop")
