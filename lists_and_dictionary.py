"""

seznam = [1, 3, 5, "string", "pipi", str("nmunu")]
print(seznam)

grill = ["bionicle", "cevapi", 40.5, 2084]
print(grill)

a = []

a.append("A")
print(a)
a.append("B")
print(a)
a.append("C")
print(a)

cars = ["toyota", "tesla", "hyundai"]

lastCar = cars.pop(1) #index, default je zadnji
print(cars)
print(lastCar)

cars.insert(-1, "audi")
print(cars)

cars.sort()
print(cars)

for car in cars:
    print(car)
"""
import datetime
import json
import random

secret = random.randint(1, 30)

attempts = 0

with open("scoreList.json", "r") as scoreFile:
    scoreList = json.loads(scoreFile.read())
    for score_dict in scoreList:
        print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date_and_time"))
    #topScore = scoreList[0] #index
    #topScores = scoreList[:3] #part of array

while True:
    guess = int(input("Guess the secret number: "))
    attempts += 1
    #attempts = attempts + 1

    if guess == secret:
        print("you have guessed it! The number is:" + str(guess))
        print("Number of attempts: " + str(attempts))
        scoreData = {
            "attempts": attempts,
            "date_and_time": str(datetime.datetime.now())
        }
        scoreList.append(scoreData)
        with open("scoreList.json", "w") as scoreFile:
            scoreFile.write(json.dumps(scoreList))
        break

    elif guess < secret:
        print("you are wrong. Try thinking bigger")

    else:
        print("you are wrong! Try thinking smaller")
        


#Dictionary
"""
box = {"height": 20,
       "width": 30,
       "length": 50
       }

box["weight"] = 1000

print(box)
print(box.get("length"))

box["price"] = 200
box["length"] = 45

print(box)

box.pop("price")

boxKeys = box.keys()

boxValues = box.values()

print(boxKeys)
print(boxValues)

"""