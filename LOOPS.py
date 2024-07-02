"""import random

secret = random.randint(a:1, b:50)
guess = None

while secret != guess:
    guess = int(input("Guess the secret number: "))
    if guess > secret:
        print("You guessed wrong! Try something smaller.")
    elif guess < secret:
        print("You guessed wrong! Try something bigger.")
    else:
        print("You guessed right!")


for x in range(5):
    guess = int(input("Guess the secret number: "))
    if guess == secret:
        print("Bravo!")
        break
    else:
        print("No!")


while True:
    print("nnnn")

"""

multiplied_value = int(input("First number:"))
upper_limit = int(input("Second number: "))

for x in range(1, upper_limit):
    y = x * multiplied_value
    if y > upper_limit:
        break
    print(y)




