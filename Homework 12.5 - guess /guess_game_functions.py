import datetime
import json
from operator import itemgetter

def open_and_print_sorted_file(file):
    with open(file, "r") as scoreFile:
        scoreList = json.loads(scoreFile.read())
        sorted_list = sorted(scoreList, key=itemgetter("attempts"))
        for score_dict in sorted_list:
            print(str(score_dict.get("attempts")) + " attempts, date: " + score_dict.get("date_and_time"))
            if score_dict == 3:
                break
def check_if_correct(guess, secret):
    if guess == secret:
        return 1
    if guess < secret:
        return 0
    else:
        return -1

def guess_feedback(result_of_guess, attempts, guess):
    if result_of_guess == 1:
        print("You are correct! The secret number is " + str(guess))
        print("Number of attempts: " + str(attempts))
    elif result_of_guess == 0:
        print("You are wrong! Try something bigger!")
    else:
        print("You are wrong! Try something smaller!")


def write_to_file(attempts, array):
    scoreData = {
        "attempts": attempts,
        "date_and_time": str(datetime.datetime.now())
    }
    array.append(scoreData)
    with open("scoreList.json", "w") as scoreFile:
        scoreFile.write(json.dumps(array))