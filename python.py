# The "print" function is used to display information
print("Hello, World!")



#  --------------------------------Variables and Data Types-------------------------------
# Variables
name = "John"
age = 25
height = 1.75

# Data Types
# String
print("Name:", name)
# Integer
print("Age:", age)
# Float
print("Height:", height)


# --------------------------------------Lists--------------------------------------------
# Lists
fruits = ["apple", "banana", "orange"]
print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])

# Adding elements
fruits.append("grape")
print("Fruits after adding grape:", fruits)


#  --------------------------------Conditions and Loops----------------------------------
# if statement
x = 10
if x > 5:
    print("x is greater than 5")

# for loop
for fruit in fruits:
    print(fruit)

# while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1
