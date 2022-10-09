from types import NoneType
from flask import Flask
import re

app = Flask(__name__)

#Prompts user to enter expressions to calculate until they exit
def main():
    user_input = input("Please enter the expression you wish to calculate: ")
    while (user_input != "exit"):
        print(calculate(user_input))
        user_input = input("Please enter the expression you wish to calculate: ")

#Takes a string and returns whether it is valid input to be calculated
def validate_input(expression):
    error_out = "error: "
    error_count = 0
    #Error States:
    #Unacceptable character (anything other than 0-9 or +-*)
    x = re.search('[^(0-9)+*-]+',expression)
    if type(x) != NoneType:
        error_out = error_out + "unexpected string character(s): " + x.group()
        error_count += 1

    #Duplicate operation
    x = re.search('([-+*]{1}\*)',expression)
    if type(x) != NoneType:
        if(error_count > 1): error_count += ", "
        error_out = error_out + "duplicate operation: " + x.group()
        error_count += 1

    #Expression begins with operation
    x = re.search('(^([-+*]{2}|\*))',expression)
    if type(x) != NoneType:
        if(error_count > 1): error_count += ", "
        error_out = error_out + "expression starts with operation: " + x.group()
        error_count += 1

    #Expression ends with operation
    x = re.search('([-+*]{1}$)',expression)
    if type(x) != NoneType:
        if(error_count > 1): error_count += ", "
        error_out = error_out + "expression ends with operation: " + x.group()
        error_count += 1

    #Return
    if(error_count == 0):
        return True
    else: return error_out
 
#Takes an expression and returns the value    
def calculate(numbers):
    validation_result = validate_input(numbers)
    if validation_result == True:
        return str(eval(numbers))
    else:
        return validation_result

if __name__ == "__main__": main()
