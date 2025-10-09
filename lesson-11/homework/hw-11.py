#Homework
#9/10/2025



# 1. Create your own virtual environment and install some python packages.
    #python -m venv myenv
    #myenv\Scripts\activate
    #source myenv/bin/activate
    #pip install numpy pandas matplotlib
    #pip list






# 2. Create custom modules.
# Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
# Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)

# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Division by zero error"

# string_utils.py
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)






# 3. Create custom packages.
# Create geometry package.
     #geometry\
     #__init__.py
     #circle.py

from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

# --- Geometry package test ---
print("Circle area:", calculate_area(5))
print("Circle circumference:", calculate_circumference(5))

# --- File operations test ---
write_file("example.txt", "Hello, Python packages!")
print("File content:", read_file("example.txt"))








