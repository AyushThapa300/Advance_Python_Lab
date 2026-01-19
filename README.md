# 1. Basic Python

Python is a high-level, interpreted, and object-oriented programming language developed by Guido van Rossum. It is widely used because of its simple syntax, readability, and versatility. Python does not require compilation; programs are executed line by line, which makes debugging easier. It supports multiple programming paradigms such as procedural, object-oriented, and functional programming. Python is commonly used in web development, data science, artificial intelligence, automation, and software development.

# 2. Data Types in Python

  Data types specify the type of data that a variable can store. Python is a dynamically typed language, meaning the data type of a variable is determined at runtime.

Common built-in data types in Python are:

int – stores whole numbers (e.g., 10, -5)

float – stores decimal numbers (e.g., 3.14, 2.5)

complex – stores complex numbers (e.g., 2+3j)

str – stores text or characters (e.g., "Python")

bool – stores Boolean values (True or False)

list – stores ordered and mutable collections

tuple – stores ordered and immutable collections

set – stores unordered unique elements

dict – stores data in key-value pairs

# 3. type() Function

The type() function is a built-in Python function used to determine the data type of a variable or value. It helps programmers understand how data is stored and processed in a program.

Syntax:

type(variable)

# 4. input() Function

The input() function is used to take input from the user during program execution. By default, the input received is of string type, even if the user enters a number.

Syntax:

variable = input("Enter a value: ")

# 5. Working of type() Function

When the type() function is applied to a variable, it returns the class of the object stored in that variable. This helps in debugging and ensures correct operations are performed on data.

Example:

a = 10
b = 2.5
c = "Python"

print(type(a))
print(type(b))
print(type(c))


Output:

<class 'int'>
<class 'float'>
<class 'str'>

# 6. Need of Typecasting with Program

Since the input() function always returns data as a string, typecasting is required to convert the input into the required data type for mathematical operations. Typecasting ensures proper calculations and avoids runtime errors.

Common typecasting functions:

int()

float()

str()

bool()

Example Program (Typecasting):

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
print("Sum =", sum)


Without typecasting, addition would result in string concatenation instead of numerical addition.

# 7. Function Syntax in Python

A function is a block of reusable code that performs a specific task. Functions help reduce code repetition and improve program readability.

Syntax:

def function_name(parameters):
    statements
    return value


Example:

def add(a, b):
    return a + b

# 8. Program to Find Area of a Rectangle

The area of a rectangle is calculated using the formula:

Area = Length × Breadth

Python Program:

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

area = length * breadth
print("Area of Rectangle =", area)


This program takes user input for length and breadth, performs multiplication, and displays the calculated area.
