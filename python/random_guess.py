import random
secret_number = random.randint(1, 100)
chances = 0
print("Guess the number between 1 and 100: ")
while True:
    guess = int(input("Enter your guess: "))
    chances += 1
    if guess == secret_number:
        print("You guessed the correct number.")
        print("You guessed the number in", chances, "chances.")
        print("You Wins!")
        break
    elif guess > secret_number:
        print("Too High")
    else:
        print("Too Low")
print("\nThe correct number was:", secret_number)