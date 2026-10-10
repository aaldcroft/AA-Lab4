# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Abby Aldcroft  
# Date:Oct 9
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# Follow the instructions from readme.md.
'''
## lab4f.py
### Using variable number of arguments with *args
- Fill in the required fields in the comment section.
- Write a function called `get_initials` that returns the first letter from each provided name. 
It can handle a variable number of name inputs.
- The function uses `*args` to accept a variable number of name inputs.
- The function iterates through each name and extract the first letter.
- The function collects these first letters into a list.
- Finally, the function returns the list of initials.
- Given the names "Alice", "Bob", "Charlie", and "David", the function will return the list `['A', 'B', 'C', 'D']`.
- Call the  `get_initials` function from `main` function and receive the result in a list variable.
- Print the result in `main`.
- Run your script to test it.
'''

def get_initials(*args): #defines intitials using multiple arguments
    initials=[] #create an empty list to append to
    for names in args: #for the multiple names entered as arguments 
        initials.append(names[0]) #append the first character
    return(initials)#return the initials to the list

def main(): #defined main
    result = get_initials("Ashley","Sarah","Tom","Steven") #arguments that will be retruned to the function
    print(result)

main() #call the function