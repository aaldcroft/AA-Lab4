# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Abby Aldcroft
# Date: oct 07 2026
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

# TO DO 1: Add the docstring
# @Function definition: add definition here
# @param: write parameters here
# @return: write return value here

# TO DO 2: Create the function.

# TO DO 3: Call the function.


def even_numbers(numbers): #creates the function

    list1 = [] #creates the empty list were going to fill

    for num in numbers: # checks each number
        if num % 2 == 0: #checks if its even
            list1.append(num) #adds even numbers
       
    return list1 #returns the completed list

numbers = [1,2,3,4,5,6,7,8] # list that is being checked

result = even_numbers(numbers)  # calling the function

print(result) #print the results 
        
