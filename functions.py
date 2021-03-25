# Functions
# Syntax to create a function: def is python keyword that tells the interpreter that a function is being declared
# def name_of_the_function():

# # Let's create a greetings function - first iteration
# def greetings():
#     print("Welcome on board")
# # If we run this program now there will be no outcome as we have not called this function
#
# # Let's see how to call this function
# greetings()

# # Greetings function second iteration to take an argument
# def greetings(name):
#     print("Welcome on board, " + name)
# # If we run this program now there will be no outcome as we have not called this function
#
# # Let's see how to call this function
# greetings("James")
# # If no argument is provided it will throw an error

# # Third iteration - create an add() to pass 2 args and add the two values
# def add(num1, num2):
#     print(num1 + num2)
#
# add(1, 2)

# Fourth iteration - to use return statement instead of print()
# def subtract(num1, num2):
#     return (num1 - num2)  # return should be the last statement
#     print("This function subtracts")  # this will not be executed
#
# print(subtract(4, 2))

# Create a calculator to add, subtract, divide, multiply
# Display appropriate messages with the computation values
def add(num1, num2):
    print("The result of this addition is")  # message confirms addition was used
    print(num1 + num2)  # result of addition


def subtract(num1, num2):
    print("The result of this subtraction is")  # message confirms subtraction was used
    print(num1 - num2)  # result of subtraction


def multiply(num1, num2):
    print("The result of this multiplication is")  # message confirms multiplication was used
    print(num1 * num2)  # result of multiplication


def divide(num1, num2):
    print("The result of this division is")  # message confirms division was used
    print(num1 / num2)  # result of division


# Check all maths functions
add(2, 2)
subtract(5, 3)
multiply(10, 3)
divide(15, 5)

# Create a greeting function by taking user input as the user name and display it with a greeting message
def greetings():
    name = input("Please enter your name ")  # define name as given by the user
    print("Hello, " + name)  # greet the user with the name provided

# Check greetings function
greetings()
