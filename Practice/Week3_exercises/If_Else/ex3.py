"""
Grade Classifier:
Create a program that asks the user to input a score (0-100) 
and then prints out the corresponding letter grade according to the following scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
"""

input_number = int(input("Enter a number between 0-100: "))

if (input_number <60):
    print("F")
elif (input_number >=60 and input_number <=69):
    print("D")
elif (input_number >=70 and input_number <=79):
    print("C")
elif (input_number >=80 and input_number <=89):
    print("B")
elif (input_number >=90 and input_number <=100):
    print("A")