'''
[expression  for loop  if condition]
'''

nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums]

print (nums)
print (nums_double)

'''
List comprehension with a condition.
'''
nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums if n % 4 == 0]

print (nums)
print (nums_double)

'''
a list comprehension which creates tuples out of the values in two lists when their sum is greater than 100. 
These tuples are the elements of the new list.
'''
list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print (sum_list)