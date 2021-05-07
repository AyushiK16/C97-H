number = 7
tries = 0
win = 0

print("Welcome to the Number Guessing Game!")


while tries <= 3 and win == 0:
    guess = int(input('Enter your guess : '))

    if guess == number:
        print("Congratulations! You guessed the number!")
        win = 1
    
    elif guess < number:
        print("The number is too low. Try again!")
        tries = tries + 1
    
    else:
        print("The number is too high. Try again!")
        tries = tries + 1


if tries > 3 and win == 0:
    print("Sorry, you lost! The correct number is", number)