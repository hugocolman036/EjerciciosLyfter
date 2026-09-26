user_input = input("Enter your numbers separated by commas: ")
numbers_list = user_input.split (',')
numbers_list = [int(num) for num in numbers_list]

# Find the smallest number
smallest = numbers_list[0]

for num in numbers_list:
    if num < smallest:
        smallest = num

# second option
smallest = min(numbers_list)

# Result
print(numbers_list)
print(f"The smallest number is {smallest}.")