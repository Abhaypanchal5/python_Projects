from random import randint

def guess_game():
    number = randint(1, 100)
    guess = 0
    no_of_guesses = 1
    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        if no_of_guesses == 10:
            print("Sorry, you've used all your guesses. The number was", number)
            return
        no_of_guesses += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
    print("Congratulations! You've guessed the number in", no_of_guesses, "guesses.")
    

guess_game()



# This is a simple number guessing game where the computer generates a random number between 1 and 100
# and the user has to guess it. 
# The user has a maximum of 10 guesses, and after each guess, 
# the program provides feedback on whether the guess is too low, too high, or correct. 
# If the user fails to guess the number within 10 attempts, the program reveals the correct number.