# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py

# Follow the instructions from readme.md.

def compute(num1,num2,operation="+"):  #defined the function
    if operation == "+": # loop to decide what opperation to use for the calculator 
        return (num1+num2)  
    elif operation == '-': 
        return (num1-num2)  
    elif operation == '*':
        return(num1*num2)
    elif operation == '/':
        return(num1/num2)

def main():

    num1= 5 #argument of 5 is taken
    num2= 3 #argument of 3 is taken
    operation = "+" #argument of +  is taken 
    # Passes the values to compute() using keyword arguments
    # Stores the returned answer in result
    result = compute(num1=num1, num2=num2, operation=operation) # result that is to be returned to the function dispite the order. 
    print(result)


if __name__ == "__main__":
    main()
