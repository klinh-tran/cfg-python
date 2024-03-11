'''
Multiplication Table
Description:
Create a program that generates and prints the multiplication table (from 1 to 10) for a given number. The program should take an input number from the user.
Extension: allow the user to specify the highest multiple to print out - e.g. 20 instead of 10.
'''
import numpy as np

'''
Create multiplication table 1..10
'''
def mult_table():
    print('** Multiplciation table **')
    for i in range(1,11):
        rows = []
        for j in range(1,11):
            rows.append(j*i)
        print(rows)

'''
Create multiplication table for the user's input number with max factor based on user's input
'''
def mult_table_user():
    number = int(input('The number to multiply: '))
    max_factor = int(input('The max multiplicaiton factor: '))
    print(f'** Multiplciation table of {number} **')
    rows = []
    for i in range(1,max_factor+1):
        rows.append(number*i)
    print(rows)

def main():
    mult_table()
    print('\r\n')
    mult_table_user()
    
if __name__ == '__main__':
    main()