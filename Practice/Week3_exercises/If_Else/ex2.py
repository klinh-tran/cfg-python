"""
Even or Odd:
Create a program that prompts the user to enter a number 
and then determines whether the number is even or odd. Print the result.
"""

input_number = int(input("Enter a number: "))

if input_number % 2 == 0:
    print("this is an even number.")
else:
    print("this is an odd number.")