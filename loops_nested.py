# Using nested for loops.

n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]

for n1 in num_list:
    for n2 in num_list: # Now we have two iterators
        if(n1 + n2 == n):
            print(n1, n2)


# Using the 'break' keyword. We terminate the loop after that using the found bool
n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]
result = ()
found = False # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if(n1 + n2 == n):
            result = (n1, n2)
            found = True # Set found to True
            break # Break inner loop if a pair is found
    if found == True:
        break # Break outer loop if a pair is found

print (result)

# Using the 'continue' keyword. 
#The loop goes into the if block when num is 3, 6, or 8. When this happens, continue is executed and the rest of the iteration, including the print() statement, is skipped.
num_list = list(range(0, 10))

for num in num_list:
  if num == 3 or num == 6 or num == 8:
    continue
  print (num)