'''
Exercise 1: Calculate the Average
Description:
You are given a list of numbers. Write a program that calculates and prints the average of all the numbers in the list.
Extension: modify the code so that it calculates the median, mode, and standard deviation as well!
'''
import math

'''
Average
'''
def average(number_list):
    total = 0
    for elem in number_list:
        total += elem
    avg = round((total / (len(number_list))),2)
    return avg

'''
Median
'''
def median(number_list):
    med_no = None
    number_list.sort()
    if len(number_list)%2 != 0:
        med_no = number_list[int((len(number_list)-1)/2)]
    else:
        no_1 = number_list[int(len(number_list)/2)]
        no_2 = number_list[int(len(number_list)/2 - 1)]
        med_no = average([no_1, no_2])
    return med_no

#########
'''
Mode
'''
def mode1(number_list):
    mode_no = None
    for elem in number_list:
        if number_list.count(elem) > number_list.count(mode_no):
            mode_no = elem
    return mode_no
    
mode2 = lambda number_list: max(number_list, key = number_list.count)  # key is the built-in param of max()
''' lambda arguments : expression '''
'''
***Explanation:
list_of_strings = ["apple", "banana", "orange"]
longest_string = max(list_of_strings, key=len)
print(longest_string)  # Output: "banana"
=> Here, `key=len` tells `max()` to use the `len()` function to determine the key value for each string in the list. The longest string in the list is returned.
'''

########
'''
standard deviation
'''
def stan_dev(number_list):
    lst = []
    for elem in number_list:
        lst.append((elem - average(number_list))**2)
    return round(math.sqrt(sum(lst)/(len(number_list)-1)) , 3)    

########
def main():
    numbers = [1,2,2,3,4,5,4,3,4,7,8]
    numbers.sort()
    print(f'List: {numbers}')
    print(f'Average is {average(numbers)}')
    print(f'Median is {median(numbers)}')
    print(f'Mode is {mode1(numbers)}')
    print(f'Mode is {mode2(numbers)}')
    print(f'Standard deviation is {stan_dev(numbers)}')

if __name__ == '__main__':
    main()