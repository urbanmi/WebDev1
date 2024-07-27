"""
inputFile = open("text.txt", "r")
# w, r, rw

contents = inputFile.read()

print(contents)

inputFile.close()

with open("text.txt", "r") as inputFile:
    contents = inputFile.read().splitlines()
# = splittedContents = contents.splitlines()
    for line in contents:
        print(line)

# file se avtomatsko zapre

with open("text.txt", "w") as outputFile:
    outputFile.write("Hello, new file!?")
    """
import random

secret = random.randint(1, 30)

attempts = 0

with open("score.txt", "r") as scoreFile:
    bestScore = int(scoreFile.read())
    print("Top score: " + str(bestScore))


while True:
    guess = int(input("Guess the secret number: "))
    attempts += 1
    #attempts = attempts = 1

    if guess == secret:
        print("you have guessed it! The number is:" + str(guess))
        print("Number of attempts: " + str(attempts))

        if attempts < bestScore:
            with open("score.txt", "w") as scoreFile:
                scoreFile.write("Top score: " + str(attempts))

        break



    elif guess < secret:
        print("you are wrong. Try thinking bigger")

    else:
        print("you are wrong! Try thinking smaller")