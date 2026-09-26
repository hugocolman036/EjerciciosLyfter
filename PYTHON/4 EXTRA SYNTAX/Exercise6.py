number = int(input("Enter a number between 1 and 10:\n "))

for i in range(1, 16): #the number 16 is not included
    result = number * i
    print(f"{number} x {i} = {result}")