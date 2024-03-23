"""
List Sum Calculator:
Write a function called sum_list() 
that takes a list of numbers as input from the user 
and calculates the sum of all the numbers in the list. 
The function should return the sum.
"""

def sum_list():
    lst_length = int(input("How many number you want to add? "))
    
    no_list = []
    for i in range(lst_length):
        elem = int(input("Enter a number: "))
        no_list.append(elem)
    print("total of the list is", sum(no_list))
    
if __name__ == "__main__":
    sum_list()