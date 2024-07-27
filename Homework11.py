import json
import random
import datetime
import operator

secret = random.randint(0, 50)

attempts = 0
wrong_guesses = []

with open("scoreList.json", "r") as scoreFile:
    scoreList = json.loads(scoreFile.read())
    sortedList = sorted(scoreList, key=lambda d: d["attempts"])
    topscoresList = sortedList[:3]
    for score_dict in topscoresList:
        print("Player Name: " + score_dict.get("playerName") + ", " + str(score_dict.get("attempts")) + " attempts, date: " + str(score_dict.get("date_and_time")))

playerName = input("Before starting the game we need to know your your player name: ")

while True:
    guess = int(input("Guess the secret number between 0 - 50?: "))
    attempts += 1

    if guess == secret:
        print("you have guessed it! The number is:" + str(guess))
        print("Number of attempts: " + str(attempts))
        scoreData = {
            "playerName": playerName,
            "attempts": attempts,
            "wrong_guesses": wrong_guesses,
            "date_and_time": str(datetime.datetime.now())
        }
        scoreList.append(scoreData)
        with open("scoreList.json", "w") as scoreFile:
            scoreFile.write(json.dumps(scoreList))
        break

    elif guess < secret:
        print("you are wrong. Try thinking bigger")
        wrong_guesses.append(guess)

    else:
        print("you are wrong! Try thinking smaller")
        wrong_guesses.append(guess)
