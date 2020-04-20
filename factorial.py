import math


def factorial(n):

    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return math.factorial(n)
    else:
        return -1
        
print(factorial(5))

# method 2 using recursion.
def factorial1(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    if n < 0:
        return -1
    # Recursive call
    return n * factorial(n - 1)

print (factorial1(5))