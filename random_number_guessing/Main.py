import random

# Getting the user's input
lower_bound = int(input("Enter Lower bound: "))
upper_bound = int(input("Enter Upper bound: "))
num_guesses = int(input("Enter number of guesses: "))

# generate and cache a number between the lower and upper bound
random_val = random.randint(lower_bound, upper_bound)
print("You have ", num_guesses, "chances to guess the random number between ",
      lower_bound, " and ", upper_bound)

# Initializing the number of guesses.
count = 0

# Allow the user to keep guessing while under the limit for number of guesses
while count < num_guesses:
    count += 1
    guess = int(input("Guess a number: "))

    # Checking if the player guessed the correct number.
    if random_val == guess:
        print("Congratulations you guessed the correct number ", random_val, " in ", count, " tries!")
        break
    elif random_val > guess:
        print("You guessed too small!")
    else:
        print("You Guessed too high!")

if count >= num_guesses:
    print("Failed to guess the random value: ", random_val, " in ", num_guesses, " attempts!")
