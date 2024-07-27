import json
import random
from guess_game_functions import check_if_correct, guess_feedback, write_to_file, open_and_print_sorted_file

secret = random.randint(1, 30)

attempts = 0

open_file(attempts)
    #topScore = scoreList[0] #index
    #topScores = scoreList[:3] #part of array

while True:
    guess = int(input("Guess the secret number: "))
    attempts += 1
    #attempts = attempts + 1

    result = check_if_correct(guess, secret)

    guess_feedback(result, attempts, guess)

    if result == 1:
        write_to_file(attempts)
        break