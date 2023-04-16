# Importing modules:

import math

x = math.sqrt(25)  # x is now 5.0

# Here are a few examples using some of the most common modules in the 
# Python Standard Library:

import collections

# Create a defaultdict
words = ["apple", "banana", "orange", "apple", "banana"]
word_counts = collections.defaultdict(int)
for word in words:
    word_counts[word] += 1

print(word_counts)  # prints {'apple': 2, 'banana': 2, 'orange': 1}

# Create a Counter
# a Counter is a dict subclass that is used to count the frequency of elements 
# in a list, tuple, or other iterable.
from collections import Counter

# Count the frequency of elements in a list
colors = ['red', 'blue', 'green', 'red', 'blue', 'yellow', 'red']
color_count = Counter(colors)
print(color_count)  # Output: Counter({'red': 3, 'blue': 2, 'green': 1, 'yellow': 1})

# Find the most common element in a list
most_common = color_count.most_common(1)
print(most_common)  # Output: [('red', 3)]

# Check if an element is in the Counter
print('red' in color_count)  # Output: True
print('purple' in color_count)  # Output: False

