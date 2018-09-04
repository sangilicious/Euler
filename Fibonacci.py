# create a list for fibonacci numbers less than 4 mil (4000000)
# Declaring Variables
num1 = 1
num2 = 2
num = 0
fib1 = [1, 2]
fib2 = []

# Creating a loop for a list of fibonacci numbers less than 4 mil
while num < 4000000:
    num = num1 + num2
    if num < 4000000:
        fib1.append(num)
        num1 = num2
        num2 = num
        continue
    else:
        break
print(fib1)

# Access this list to iterate and create a new list that has only even numbers from this list
for i in fib1:
    if i % 2 == 0:
        fib2.append(i)
        continue
    else:
        continue
print(fib2)

# find the sum of even numbers from this new list
print(sum(fib2))