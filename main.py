import random

import functions

print("Enter highest possible number:")
highest_num = int(functions.not_valid_number(input()))

print(f"Guess the number between 1 and {highest_num}:")

value_to_guess = random.randint(1, highest_num)
valid_num = int(functions.not_valid_number(input()))
number = int(valid_num)
functions.guess_num_func(value_to_guess, number)
