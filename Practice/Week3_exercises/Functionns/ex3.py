"""
Maximum Number Finder:
Write a function called find_max() 
that takes a list of numbers as input from the user 
and returns the maximum number in the list.
"""

def find_max():
    lst_length = int(input("How many number you want to add? "))
    
    no_list = []
    for i in range(lst_length):
        elem = int(input("Enter a number: "))
        no_list.append(elem)
    print("the biggest number in the list is", max(no_list))
    
if __name__ == "__main__":
    find_max()
    
##### think about using split()