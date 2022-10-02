import random

num = int(input("The value: "))

while True:
    guess = random.randint(1, 9)

    if abs(num - guess) >= 5:
        print(f"Guess: {guess}", end=" is ")
        print("Too high or low")
    elif abs(num - guess) >= 2:
        print(f"Guess: {guess}", end=" is ")
        print("High or low")
    elif abs(num - guess) == 1:
        print(f"Guess: {guess}", end=" is ")
        print("Nearby")
    elif guess == num:
        print(f"Guess: {guess}", end=" ")
        print("Got it")
        break

