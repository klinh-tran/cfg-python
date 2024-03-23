'''
While Loop
Description:
Create an empty list, and while the number of entries in the list is less than 10, add multiples of 3 to the list. 
When the list is full of 10 entries, print the whole list.
Extension: For each iteration of the while loop, print the total of all the items in the list.
'''
import random

lst = []
while len(lst)<10:
    number = int(input('Enter a number: '))
    if number <10:
        lst.append(number*3)
    else:
        lst.append(number)
    print(f'Sum of the current list: {sum(lst)}')
print(f'The whole list: {lst}')