# Add comments before you do anything else.
#!/usr/bin/env python3
# Author:Abby Aldcroft
# Date:Oct 9 2026
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# Follow the instructions from readme.md.

def sum(num1,num2): #creates the function with 2 parameters 
    return num1 + num2 # adds the 2 numbers and returns the sum

def main(): # where the input and answer will be received 

    num1 = int(input("please provide a number: ")) #prompt for user input
    num2 = int(input("please provide another number: "))#prompt for user input

    result = sum(num1,num2) #stores the returned answer in result

    print(result)   # prints result

if __name__ == "__main__":
    main()
