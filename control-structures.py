# Control Structures
# if-else statement, for loop, and while loop
x = 10

#### if statement
if x > 0:
    print("x is positive")
else:
    print("x is not positive")

if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")


# Loops

#### for loop
for i in range(5):
    print(i)

#### while loop
i = 0

# loop runs as long as the condition is true
while i < 5:
    # execute the code in the loop
    print(i)
    
    # update the loop variable to change the condition
    i += 1
