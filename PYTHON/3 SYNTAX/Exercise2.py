name = input ("what is your name?\n")
last_name = input ("what is your last name?\n")
age = int (input ("what is your current age?\n"))
sex = input ("write your sex (M/F):\n").upper()
# Condition 1
if age <= 2:
    message = "a baby"
elif age <= 9:
    message = "a big kid"
elif age <= 12:
    message = "a pre-teenager"
elif age <= 17:
    message = "a teenager"
elif age <= 35:
    message = "a young adult"
elif age <= 59:
    message = "an adult"
else:
    message = "an elderly person"
# Condition 2
if sex == "M":
    pronoun = "He"
elif sex == "F":
    pronoun = "She"
else:
    pronoun = "They"

print (f"{name} {last_name} is {age} years old. {pronoun} is {message}.")