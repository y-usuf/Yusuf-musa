
def rep_cat(x, y):

    result1 = str(x) * 10                           # value of x converted to string and repeated 10 times
    result2 = str(y) * 5                            # value of y converted to string and repeated 5 times
    output = "{0}{1}".format(result1,result2)       # concantenate the string value of y to the value of x

    return output

# Allow user to input values of x and y
x = input('')
y = input('')


result = rep_cat(x,y) 
print(result)



# Method 2 of doing it.
def rep_cat2(x, y):
    return str(x) * 10 + str(y) * 5

print (rep_cat2(3, 4))