total_sum = 0
counter = 1
num = int(input("Enter a number:"))

# Condition
while counter <= num:
    total_sum += counter #total_sum = total_sum + counter
    counter += 1 #remember counter = counter + 1
    
# Results
print("The sum of the numbers from 1 to", num, "is:", total_sum)