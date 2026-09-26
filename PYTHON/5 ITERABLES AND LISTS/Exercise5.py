numbers = []
counter = 1

# first option

while counter <= 10:
    num = int(input(f"Enter number {counter}: "))
    numbers.append(num)

    counter += 1

# second option

for counter in range(1, 11):
    num = int(input(f"Enter number {counter}: "))
    numbers.append(num)

# the highest number
highest = max(numbers)

# second option for the highest number
highest = numbers[0]

for num in numbers:
    if num > highest:
        highest = num

print(f"Numbers entered: {numbers}")
print(f"The highest number was {highest}.")