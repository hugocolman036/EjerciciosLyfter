user_input = input("Enter your numbers separated by commas: ")
numbers_list = user_input.split(',')
numbers_list = [int(num) for num in numbers_list]

# Calculate the sum of the numbers of the list
total_sum = 0
for num in numbers_list:
    total_sum += num

# Average
count_numbers = len(numbers_list)
average = total_sum / count_numbers

# Create a new list with numbers greater than the average
greater_than_average = []

for num in numbers_list:
    if num > average:
        greater_than_average.append(num)

# Results
print(numbers_list)
print(f"Average: {average}")
print(f"Numbers greater than the average: {greater_than_average}")