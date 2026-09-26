print("Guess the secret number between 1 and 10!")
# Random
import random
secret_number = random.randint(1, 11)
# Condition
while True:
    try_number = int(input("Enter a number between 1 and 10:"))
    if try_number == secret_number:
        print("Congratulations! You got the number!")
        break
    elif try_number < secret_number:
        print("The number that you are looking for is higher, try again!")
    else:
        print("The number is smaller, try one more time!")