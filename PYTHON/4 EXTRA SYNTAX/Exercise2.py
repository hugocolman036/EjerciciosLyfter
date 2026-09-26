sec_time = int(input("Enter the time in seconds:\n"))

# Condition
if sec_time < 600:
    remaining_time = 600 - sec_time
    print("It is missing", remaining_time, "seconds to reach 10 min")
elif sec_time > 600:
    print("The time is higher!")
else:
    print("The time is the same!")