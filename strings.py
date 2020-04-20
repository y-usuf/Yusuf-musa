# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# concatenate (Insert a variable into a string)
#print('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by position.
#print('My name is {name} and I am {age}'.format(name=name, age=age ))

# F-strings
#print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# get lenght
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# End with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

