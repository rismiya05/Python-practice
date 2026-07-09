secret_number = 26

while True:
    guess_number = int(input("Guess a number between 1 to 50: "))

    if guess_number == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess_number <= 10:
        print("Your guess is too low. Try again.")

    elif guess_number <= 20:
        print("Your guess is a bit low. Try again.")

    elif guess_number <= 30:
        print("Your guess is very close. Try again.")

    elif guess_number <= 40:
        print("Your guess is a bit high. Try again.")

    elif guess_number <= 50:
        print("Your guess is too high. Try again.")

    else:
        print("Sorry, that's not the correct number.")