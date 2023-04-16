# Interacting with the operating system: 
# 
# The os module provides a number of functions for interacting with the 
# operating system, such as navigating the file system and launching 
# external programs. For example:

import os

# Get the current working directory
cwd = os.getcwd()
print(cwd)  # prints the current working directory

# List the files in a directory
files = os.listdir(".")
print(files)  # prints a list of the files in the current

# Launch the "TextEdit" program on macOS
os.system('open -a TextEdit')


# Alternatively, you can use the subprocess module to launch external programs. 
import subprocess

# Launch the "TextEdit" program on macOS and capture its output
result = subprocess.run(['open', '-a', 'TextEdit'], capture_output=True)
print(result.stdout)  # Output: the TextEdit program's output
