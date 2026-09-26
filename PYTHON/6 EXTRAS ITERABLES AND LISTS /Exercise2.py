user_input = input("Enter your numbers separated by commas: ")
numbers_list = user_input.split (',')
numbers_list = [int(num) for num in numbers_list]

# Verify if all numbers are positive
all_positive = True

for num in numbers_list:
    if num <= 0:
        all_positive = False
        break

# function all
all_positive = all(num > 0 for num in numbers_list)

# Result
print(numbers_list)

if all_positive:
    print("All elements are positive.")
else:
    print("At least there is a negative element or zero")