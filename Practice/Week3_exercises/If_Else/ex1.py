"""
Number Comparison:
Write a Python program that takes two numbers as input from the user 
and prints out whether the first number is greater than, equal to, or less than the second number.
"""

no_1 = int(input("Enter the first number: "))
no_2 = int(input("Enter the second number: "))

if no_1 < no_2:
    print("the first number is less than the second number.")
elif no_1 == no_2:
    print("the frist number equals to the second number.")
else: 
    print("the first number is more than the second number")