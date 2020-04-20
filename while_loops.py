#while loop that finds out the maximum power of n before the value exceeds 1000:

'''
In each iteration, we update val and check if its value is less than 1000. 
The value of power tells us the maximum power n can have before it becomes greater than 1000. 
Think of it as a counter.

'''

n = 5 # Could be any number
power = 0
val = n
while val < 1000:
  power += 1
  val *= n
print (power)

'''
We can also use while loops with data structures, especially in cases where the length of data structure changes during iterations.
'''
n = 249
last = n % 10 # Finding the last number is easy

first = n # Set it to `n` initially
while first >= 10:
  first //= 10 # Keep dividing by 10 until the leftmost digit is reached.

result = first + last
print (result)