import random

num_1 = random.randint(1, 100)

num_2 = int(input("Please guess a number: "))

while True:
    if num_2 < 1 or num_2 > 100:
        num_2 = int(input("Out of bounds! Please guess a number between 1 and 100: "))
        continue

    if num_2 == num_1:
        print("Congratulations! You guessed the correct number.")
        break

    if num_2 < num_1:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    num_2 = int(input("Please guess a number: "))
    if num_2 > num_1:
        print("Your guess is too high.")
        num_2 = int(input("Please guess a number: "))



