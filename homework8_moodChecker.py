#Homework 8.1

mood = input("How is your day going?")

if mood == "good" or mood == "great":
    print("You're having a great day!")

elif mood == "not terrible" or mood == "not great":
    print("You're having a great day")

else:
    print("I'm sorry you're having a bad day!")


#Homework 8.2

secret = 3

guess = input("Guess the number")

guess = int(guess)

if secret == guess:
    print("You were right! You win a million dollars!")
else:
    print("Wrong! Try again")

#Homework 8.3

x = input("First value of equation: ")

op = input("Arithemtic operation: ")

y = input("Second value of equation: ")

x = int(x)
y = int(y)

if op == "+":
    print("Added value: ")
    print(x+y)
elif op == "-":
    print("Subtracted value: ")
    print(x-y)
elif op == "*":
    print("Multiplied value: ")
    print(x*y)
elif op == "/":
    print("Divided value: ")
    print(x/y)
else:
    print("Unknown arithmetic operation.")