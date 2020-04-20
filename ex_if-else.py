

# n = int(input("Enter n: "))

# if n % 2 != 0:
#     print('Weird')
# elif n % 2 == 0 and n in range(2,6):
#     print('Not Weird') 
# elif n % 2 == 0 and n in range(6,21):
#     print('Weird')
# elif n in range(1,101):
#      print('Not Weird')

n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])