# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
# for person in people:
#     print(f'Current Person: {person}')

# Break (stops the loop when it gets to Sara)
# for person in people:
#     if person == 'Sara':
#         break
#     print(f'Current Person: {person}')

# Continue (doesn't stop the loop when gets to Sara, skips her and continues)
# for person in people:
#     if person == 'Sara':
#         continue
#     print(f'Current Person: {person}')

# range
# for i in range(len(people)):
#     print(people[i])

# for i in range(0, 11):
#     print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1

# Looping through a range
for i in range(1,11): # A sequence from 1 to 10
    if i % 2 == 0:
        print (i, " is even")
    else:
        print (i, " is odd")

# Looping through a string and iterating through its indices.
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print (float_list)

for i in range(0, len(float_list)): # Iterator goes traverses to the last index of the list
  float_list[i] = float_list[i] * 2

print (float_list)

# Example 2
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for num in float_list: # Iterator goes traverses to the last index of the list
  if num > 10:
    count_greater += 1

print (count_greater)