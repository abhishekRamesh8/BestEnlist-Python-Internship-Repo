# 	Write a Python program to map two lists into a dictionary

hdr_table = ["Name", "ID", "Lecture", "Grade"]
record = ["R. Abhishek", "21101", "Programming", "A"]

dt_student = dict(zip(hdr_table, record))

print(dt_student)