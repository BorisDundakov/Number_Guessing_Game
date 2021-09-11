def not_valid_number(number):
    while not str(number).isdigit():
        print("Please enter a number!")
        number = input()
    return number


def guess_num_func(value_to_guess, number):
    while number != value_to_guess:

        result = not_valid_number(number)

        if int(result) < value_to_guess:
            print("Incorrect! Guess a higher number.")
        elif int(result) > value_to_guess:
            print("Incorrect! Guess a lower number.")
        else:
            print("Congratulations! You guessed the correct number!")
            exit()

        number = input()
    print("Congratulations! You guessed the correct number!")

    exit()
