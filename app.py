from flask import Flask

app = Flask(__name__)

#Prompts user to enter expressions to calculate until they exit
def main():
    user_input = input("Please enter the expression you wish to calculate: ")
    print(user_input)
    while (user_input != "exit"):
        print(calculate(user_input))

        user_input = input("Please enter the expression you wish to calculate: ")
        print(user_input)

#Takes a string and returns whether it is valid input to be calculated
def validate_input(expression):
    return True
 
#Takes an expression and returns the value    
def calculate(numbers):
    if validate_input(numbers) == True:
        return str(eval(numbers))
    else:
        return "Invalid Input" 

if __name__ == "__main__": main()
