# 	print one message if the try block raises a NameError and another for other errors

try:
    print(a)
except NameError:
    print("Variable not defined")
except:
    print("Exception")
