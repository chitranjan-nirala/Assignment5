# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

Stu_ditrctory = {'aman':'12', 'alice':'89', 'jhon':'90'}
s_name  = input("Enter the Student's name :")
if s_name in Stu_ditrctory:
 print("{}'s marks :{}" .format(s_name, Stu_ditrctory.get(s_name)))
else:
    print(" Student not found")