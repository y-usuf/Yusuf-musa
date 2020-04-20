# Recursion is the process in which a function calls itself during its execution. Each recursive call takes the program one scope deeper into the function.

# Let’s write a function which decrements a number recursively until the number becomes 0:
def rec_count (number):
  print (number)
  # Base case
  if number == 0:
    return 0
  rec_count (number - 1) # A recursive call with a different argument
  print (number)

rec_count (5)
