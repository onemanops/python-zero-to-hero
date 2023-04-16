# Functions
# Functions group together related code that can easily be reused

# A function that takes one argument and prints it out
def greet(name):
    print("Hello, " + name + "!")

# A function that takes two arguments and returns their sum
def add(a, b):
    return a + b

# A function that takes a list and returns the sum of its elements
def sum_list(lst):
    total = 0
    for number in lst:
        total += number
    return total

# A function that takes a string and returns it in uppercase
def to_uppercase(string):
    return string.upper()

# A function that takes no arguments and returns the current time
from datetime import datetime
def get_current_time():
    return datetime.now()

# To call a function, you can use its name followed by parentheses and any necessary arguments. 
# 
# For example:
greet("Alice")  # prints "Hello, Alice!"
result = add(1, 2)  # result is 3
numbers = [1, 2, 3, 4, 5]
total = sum_list(numbers)  # total is 15
uppercase_string = to_uppercase('hello')  # uppercase_string is 'HELLO'
time = get_current_time()  # time is the current time
print(f'results: {result}, numbers: {numbers}, total: {total} upper: {uppercase_string}, time: {time}')