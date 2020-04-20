# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

#print(fruits, fruits2)

# Single value needs trailing comma
fruits2 = ('Apples',)
#print(fruits2, type(fruits2))

# Get value
print(fruits[1])

# Can't change value
#fruits[0] = 'Pears'

# Delete tuple
del fruits2

print(len(fruits))




# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in a set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Remove from set
fruits_set.remove('Grapes')

# Add to set
fruits_set.add('Apples')  # Doesn't add apple twice, already there

# Clear set
#fruits_set.clear()       # Clear values in the set

# Delete
#del fruits_set           # not defining it completely

print(fruits_set)



