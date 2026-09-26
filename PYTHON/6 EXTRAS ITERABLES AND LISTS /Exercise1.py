user_input = input("Enter your numbers separated by commas: ")
numbers_list = user_input.split(',')
numbers_list = [int(num) for num in numbers_list]

# Other way to create a list

# new_list = []

# for num in numbers_list:
    # new_list.append(int(num))

# numbers_list = new_list


# Print the numbers entered by the username
print(numbers_list)

# Number to find in the list
number_to_find = int(input("Enter the number to find in the list: "))
repeated_count = numbers_list.count(number_to_find)

# Second Option
repeated_count = 0

for num in numbers_list:
    if num == number_to_find:
        repeated_count += 1

if repeated_count == 0:
    print(f"The number {number_to_find} is not in the list.")
else:
    print(f"The number {number_to_find} appears {repeated_count} time(s).")
