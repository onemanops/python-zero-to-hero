# Lists
# 
# create a list
numbers = [1, 2, 3, 4, 5]

# access values using indexes
print(numbers[0])  # prints 1
print(numbers[3])  # prints 4

# modify values in the list
numbers[2] = 6

# add a new item to the end of the list
numbers.append(7)

# insert an item at a specific position in the list
numbers.insert(3, 10)

# remove an item from the list
numbers.remove(4)

# find the length of the list
print(len(numbers))  # prints 6

# loop through the list
for number in numbers:
    print(number)
