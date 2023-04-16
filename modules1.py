# Reading and writing files: 
# The io module provides a number of functions for reading and writing files. 
# 
import io

# Write to a file
with io.open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world!\n")

with io.open("test.txt", "a", encoding="utf-8") as f:
   f.write("Hello, world!")

# Read from a file
with io.open("test.txt", "r", encoding="utf-8") as f:
    text = f.read()
    f.seek(0)
    lines = f.readlines() # returns a list of lines
print(text)  # prints "Hello, world!"


# print one line at a time
for line in lines:
  print(line)

# shorthand aka list comprehension
[ print(line) for line in lines ]  # iterates over lines and prints each element
