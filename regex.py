# Regular Expressions

import re

# Replace a pattern
pattern = r'cat'
text = 'The cat in the hat.'
new_text = re.sub(pattern, "dog", text)
print(new_text)  # prints "The dog in the hat."

# Check if a string contains a certain pattern
string = "The quick brown fox jumps over the lazy dog."
pattern = "fox"
if re.search(pattern, string):
    print("Match found!")
else:
    print("Match not found.")

# Find all occurrences of a pattern in a string
string = "The quick brown fox jumps over the lazy fox."
pattern = "fox"
matches = re.findall(pattern, string)
print(matches)  # Output: ['fox', 'fox']

# Replace all occurrences of a pattern in a string
string = "The quick brown fox jumps over the lazy dog."
pattern = "fox"
replacement = "cat"
new_string = re.sub(pattern, replacement, string)
print(new_string)  # Output: "The quick brown cat jumps over the lazy dog."

# Split a string based on a pattern
string = "The quick brown fox jumps over the lazy dog."
pattern = "the"
words = re.split(pattern, string, flags=re.I)
print(words)  # Output: ['The quick brown fox jumps over ', ' lazy dog.']
