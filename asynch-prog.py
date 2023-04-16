# Asynchronous programming: 
# 
# Asynchronous programming allows you to perform multiple tasks concurrently, 
# which can improve the performance of your programs and make them more 
# efficient. Python has a number of tools for asynchronous programming, 
# including the asyncio module and the async and await keywords. 
# 
# For example:


import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(1)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2()) 

asyncio.run(main())


# When you run this code, the output will look something like this:
'''Task 1 started
Task 2 started
Task 1 completed
Task 2 completed'''

# You can see that both tasks start simultaneously and complete at different 
# times, as they are running concurrently.