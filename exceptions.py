# Exceptions - use try and except statements to catch exceptions and take appropriate action.

# This code will raise a ZeroDivisionError exception 
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")  # Output: "You can't divide by zero!"

# This code will raise an IndexError exception  because the list has only two elements and we're trying to access the third
try:
    numbers = [1, 2]
    print(numbers[2])
except IndexError:
    print("Index out of range!")  # Output: "Index out of range!"

# This code will raise a ValueError exception because the int() function can't convert the string 'abc' to a number
try:
    int('abc')
except ValueError:
    print("Invalid literal for int()")  # Output: "Invalid literal for int()"

# This code will raise a FileNotFoundError exception because the file 'myfile.txt' doesn't exist
try:
    with open('myfile.txt', 'r') as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found!")  # Output: "File not found!"

# You can also specify multiple exceptions to catch
try:
    int('abc')
    5 / 0
    numbers = [1, 2]
    print(numbers[2])
except (ValueError, ZeroDivisionError, IndexError):
    print("An error occurred!")  # Output: "An error occurred!"
