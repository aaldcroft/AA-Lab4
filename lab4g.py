# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

# Follow the instructions from readme.md.

'''
Create a variable list named numbers containing numbers from 2 to 10.
square all elements of this list using map and lambda function.
Print variable numbers.
Make a new variable named divisible_by_2.
Filters out all numbers from numbers list that are divisible by 2 using filter and lambda, and save them in this variable.
Print variable divisible_by_2.
'''

numbers = [2,3,4,5,6,7,8,9,10] #list of numbers

numbers = list(map(lambda num: num ** 2,numbers)) # replace original number list with squared values 


print(numbers)

divisible_by_2 = list(filter(lambda num:num % 2 == 0,numbers))#keep only the elements that meet the condition

print(divisible_by_2)