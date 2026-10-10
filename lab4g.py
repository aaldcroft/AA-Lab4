# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Abby Aldcroft
# Date:Oct 9
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

# Follow the instructions from readme.md.


numbers = [2,3,4,5,6,7,8,9,10] #list of numbers

numbers = list(map(lambda num: num ** 2,numbers)) # replace original number list with squared values 


print(numbers)

divisible_by_2 = list(filter(lambda num:num % 2 == 0,numbers))#keep only the elements that meet the condition

print(divisible_by_2)