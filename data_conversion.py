# Converting to a list.
# We can convert a tuple, set, or dictionary to a list using the list() constructor. In the case of a dictionary, only the keys will be converted to a list.
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print (star_wars_tup)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print (star_wars_set)
star_wars_dict = {1:"Anakin", 2:"Darth Vader", 3:1000}
print (star_wars_dict)

star_wars_list = list(star_wars_tup) # Converting from tuple
print(star_wars_list)

star_wars_list = list(star_wars_set) # Converting from set
print(star_wars_list)

star_wars_list = list(star_wars_dict) # Converting from dictionary
print(star_wars_list)

'''
Converting to tuples.
Any data structure can be converted to a tuple using the tuple() constructor. 
In the case of a dictionary, only the keys will be converted to a tuple:
'''
star_wars_list = ["Anakin", "Darth Vader", 1000]
print (star_wars_list)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print (star_wars_set)
star_wars_dict = {1:"Anakin", 2:"Darth Vader", 3:1000}
print (star_wars_dict)

star_wars_tup = tuple(star_wars_list) # Converting from list
print(star_wars_tup)

star_wars_tup = tuple(star_wars_set) # Converting from set
print(star_wars_tup)

star_wars_tup = tuple(star_wars_dict) # Converting from dictionary
print(star_wars_tup)

'''
Converting to a set.
The set() constructor can be used to create a set out of any other data structure. 
In the case of a dictionary, only the keys will be converted to a set:
'''
star_wars_list = ["Anakin", "Darth Vader", 1000]
print (star_wars_list)
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print (star_wars_tup)
star_wars_dict = {1:"Anakin", 2:"Darth Vader", 3:1000}
print (star_wars_dict)

star_wars_set = set(star_wars_list) # Converting from list
print(star_wars_set)

star_wars_set = set(star_wars_tup) # Converting from tuple
print(star_wars_set)

star_wars_set = set(star_wars_dict) # Converting from dictionary
print(star_wars_set)

'''
Converting to a dictionary.
The dict() constructor cannot be used in the same way as the others because it requires key-value pairs instead of just values. 
Hence, the data must be stored in a format where pairs exist.
'''
star_wars_list = [[1,"Anakin"], [2,"Darth Vader"], [3, 1000]]
print (star_wars_list)
star_wars_tup = ((1, "Anakin"), (2, "Darth Vader"), (3, 1000))
print (star_wars_tup)
star_wars_set = {(1, "Anakin"), (2, "Darth Vader"), (3, 1000)}
print (star_wars_set)

star_wars_dict = dict(star_wars_list) # Converting from list
print(star_wars_dict)

star_wars_dict = dict(star_wars_tup) # Converting from tuple
print(star_wars_dict)

star_wars_dict = dict(star_wars_set) # Converting from set
print(star_wars_dict)