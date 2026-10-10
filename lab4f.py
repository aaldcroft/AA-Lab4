# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Abby Aldcroft  
# Date:Oct 9
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# Follow the instructions from readme.md.

def get_initials(*args): #defines intitials using multiple arguments
    initials=[] #create an empty list to append to
    for names in args: #for the multiple names entered as arguments 
        initials.append(names[0]) #append the first character
    return(initials)#return the initials to the list

def main(): #defined main
    result = get_initials("Ashley","Sarah","Tom","Steven") #arguments that will be retruned to the function
    print(result)

main() #call the function