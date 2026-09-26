import random
secret_number = random.randint (1, 10)
# Condition to execute the loop
guessed_number = True

print ("Welcome to the Secret Number Guessing")
# try word cannot be a variable in Python (not recognized)
while guessed_number:
    try_number = int(input("Guess the secret number between (1 and 10):"))
    if try_number == secret_number:
        print("Congratulations! You guessed the secret number")
        guessed_number = False
    else:
        print("Incorrect, try again!")


#second option using break
import random

secret_number = random.randint(1, 10) #numbers 1 and 10 are included

print("Welcome to the Secret Number Guessing")

while True:
    try_number = int(input("Guess the secret number between (1 and 10): "))

    if try_number == secret_number:
        print("Congratulations! You guessed the secret number")
        break #the loop stop when the number to guess is found 
    else:
        print("Incorrect, try again!")