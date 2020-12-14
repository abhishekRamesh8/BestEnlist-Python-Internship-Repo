# 	Write a Python program to remove the intersection of a 2nd set from the 1st set

dt_python_class = {'Abhishek', 'yogesh', 'meeran', 'sathish', 'sreekanth'}

dt_frontend_class = {"vicky", "meeran", "john", "michael", "sathish", "thomas", "andreas"}

enroll_two_class = dt_frontend_class & dt_python_class

print(enroll_two_class)

print(dt_python_class - dt_frontend_class)

print(dt_frontend_class - dt_python_class)