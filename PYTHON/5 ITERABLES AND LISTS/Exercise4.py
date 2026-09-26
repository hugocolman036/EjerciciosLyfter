# First List
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Even numbers
filtered_list = [num for num in my_list if num % 2 == 0]

# Result
print(filtered_list)

# Another option for even numbers
filtered_list =  []

for num in my_list:
    if num % 2 == 0:
        filtered_list.append(num)
    
print(filtered_list)



# Odd numbers
filtered_list =[num for num in my_list if num % 2 != 0]

# Another option for odd numbers
filtered_list =  []

for num in my_list:
    if num % 2 != 0:
        filtered_list.append(num)
    
print(filtered_list)

# Result
print(filtered_list)