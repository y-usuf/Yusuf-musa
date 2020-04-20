# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create a dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use a constractor
#person2 = dict(first_name='Sarah', last_name='Williams')

#print(person, type(person))

# Get Value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone']= '0713-447-395'

# Get dict keys
print(person.keys())

#Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Nairobi'

# Remove and item
del(person['age'])
person.pop('phone')

# clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

#print(people)
print(people[0]['name'])


# Copying content from one dictionary to another
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print (phone_book)

# Dictionary comprehension
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2:house+"!" for (n, house) in houses.items()}
print (houses)
print (new_houses)
