# ----------------------Variables: 
# Variables are containers for storing data values
#    Variables in Python are used to store data values. 
#    A variable is created the moment you first assign a value to it. Variable names in Python can contain letters, numbers, and underscores but cannot start with a number. They are case-sensitive.

x = 10
name = "John"
is_active = True



# ---------------------Functions: 
# Functions are blocks of reusable code that perform a specific task. 
#   They provide modularity and help in code organization. 
#   In Python, you define a function using the def keyword followed by the function name, parameters (if any), and a colon. 
#   Functions can take inputs, perform operations, and optionally return a result using the return statement.

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8


# ---------------------Lists:
# Lists are ordered collections of items in Python. 
#   They are mutable, meaning their elements can be changed after creation. 
#   Lists are defined using square brackets [] and can contain elements of different data types, including other lists.

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]




# ---------------------Dictionaries: 
# Dictionaries are unordered collections of key-value pairs in Python. 
#   They are mutable and are defined using curly braces {}. 
#   Each element in a dictionary consists of a key-value pair, where the key is unique and used to access its associated value. 
#   Dictionaries are commonly used for mapping relationships between items.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict['age'])  # Output: 30



# --------------------Control Flow Statements: 
#   Control flow statements are used to control the flow of execution in a program. 
#   They include conditional statements like if, elif, and else, which allow you to execute different blocks of code based on certain conditions. 
#   Python also provides looping constructs like for and while, which allow you to iterate over sequences of data.


x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")



# --------------------Classes and Objects: 
#   Classes and objects are fundamental concepts in object-oriented programming (OOP)
#   A class is a blueprint for creating objects, which are instances of that class
#   Classes define attributes (data) and methods (functions) that operate on that data
#   Objects encapsulate data and behavior and promote code reuse and modularity.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

person1 = Person("John", 30)
person1.greet()  # Output: Hello, my name is John


# ----------------------Modules and Packages: 
#    Modules are Python files containing Python code, typically grouped together based on functionality. 
#    They allow you to organize your code into reusable components and provide namespaces to avoid naming conflicts. 
#    Packages are directories containing multiple modules and an __init__.py file, which indicates that the directory should be treated as a package.

# Contents of my_module.py
def my_function():
    print("This is my function in my_module.py")

# Using the module
import my_module
my_module.my_function()  # Output: This is my function in my_module.py



# ------------------------Exceptions: 
# Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. 
# When an exception occurs, it can be caught and handled using try and except blocks, allowing you to gracefully recover from errors. 
# Python provides built-in exception types for common error conditions, and you can also define custom exception classes to handle specific situations.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")



# String is a sequence of characters enclosed within either single quotes (') or double quotes ("). 
#     Python treats single and double quotes the same way, so you can use either depending on your preference or to handle situations where one type of quote appears within the string.
    
my_string1 = "Hello, World!"
my_string2 = 'Python is awesome'
my_string3 = "It's raining today"

# Multiline string using triple quotes
multiline_string = """This is a 
multiline 
string"""

# Accessing characters in a string
first_char = my_string1[0]  # Accessing the first character
substring = my_string1[7:12]  # Accessing a substring

# Concatenating strings
concatenated_string = my_string1 + " " + my_string2

# String formatting
formatted_string = "My name is {} and I am {} years old".format("Alice", 30)
