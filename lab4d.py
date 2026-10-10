# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Abby Aldcroft
# Date:Oct 09
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py
# Follow the instructions from readme.md.

def compute(num1,num2,operation="+"): #defines the function
    if operation == "+": #if addition is chosen
        return (num1+num2) # return the addition 
    elif operation == '-': # if subraction is chosen 
        return (num1-num2) # return the subtraction 
    elif operation == '*':
        return(num1*num2)
    elif operation == '/':
        return(num1/num2)

def main():
    num1 = int(input("Enter the first number: ")) #user input 
    num2 = int(input("Enter the second number: "))
    operation = input("chose an operation ( +, - , * , /) : ")

    result = compute(num1,num2,operation) #where the return result is stored
    print(result)

main()


    
