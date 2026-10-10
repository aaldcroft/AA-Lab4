# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Abby Aldcroft
# Date: Oct 07 2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
# @param: write parameters here
# @return: write return value here 

# TO DO 2: define the function with name `is_even`.

# TO DO 3: Call the function `is_even`.

num_list= [] #create empty list to store values in 

def is_even(num_list):
#checks if the user input an even or odd number
    return_value = False # return value is false

    for num in num_list: # for the numbers in the list

        if num % 2 == 0: # if remainder = 0
            rerun_value = True#then true
            break #break if ture
    
    return return_value #all else return false

list1 = [2,4,3,7,3,9]   # list of numbers
result = is_even(list1) # return the result to function is even

print(result)



  





