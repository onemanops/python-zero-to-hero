# List comprehension




# Here is an example of using list comprehension to create a list of the squares
# of the numbers from 1 to 10:

# Traditional looping
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares) # prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''Using list comprehension'''
squares = [i**2 for i in range(1, 11)]
print(squares) # prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]




# an example of using list comprehension to filter out even numbers and double 
# the remaining odd numbers

# Traditional looping
odd_doubles = []
for i in range(1, 11):
    if i % 2 == 1:
        odd_doubles.append(i * 2)
print(odd_doubles)

'''Using list comprehension'''
odd_doubles = [i * 2 for i in range(1, 11) if i % 2 == 1]
print(odd_doubles)
