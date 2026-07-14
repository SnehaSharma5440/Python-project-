import random

number = random.randint(1, 20)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 20.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number:
        print("Correct! You guessed it in", attempts, "attempt(s).")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    