# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name = 'Sam'):
    print(f'Hello {name}')

sayHello()

# Create another function
def minimum (first, second):
    if (first < second):
        print (first)
    else:
        print (second)

num1 = 10
num2 = 20

minimum (num1, num2)

#Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

num = getSum(3,4)
print(num)

# A lambda function is a small anonymous function.
triple = lambda num : num * 3 # Assigning the lambda to a variable
print (triple(10)) # Calling the lambda and giving it a parameter

# A lambda that concatenates the first characters of three strings together. 
concat_strings = lambda a, b, c : a[0] + b[0] + c[0]
print (concat_strings("World", "Wide", "Web"))

# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
def calculator(operation, n1, n2):
    return operation(n1, n2)  # Using the 'operation' argument as a function


# 10 and 20 are the arguments.
result = calculator(lambda n1, n2: n1 * n2, 10, 20)

# The lambda multiplies them.
print (result)

print (calculator(lambda n1, n2: n1 + n2, 10, 20))

# Another example.

getSum = lambda num1, num2 : num1 + num2

print(getSum(10,3))

# Using map function on lambda
num_list = [0, 1, 2, 3, 4, 5]

double_list = map (lambda n : n * 2, num_list)

print (list(double_list))

# Using the filter function. Filters all numbers above 10. The function returns a filter object which can be converted to a list using list().
numList = [30, 2, -15, 17, 9, 100]

greater_than_10 = list(filter(lambda n : n > 10, numList))
print (greater_than_10)