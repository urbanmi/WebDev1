import random
import numpy as np
def generate_field(game_size, init):
    game_area = [[init for x in range(game_size)] for y in range (game_size)]
    return game_area

def generate_point(game_size):
    x = random.randrange(0, game_size)
    y = random.randrange(0, game_size)

    return x, y

def generate_point_ships(game_area, game_size):
    tons = int(pow(game_size, 2) * 0.2)
    for points in range(tons):
        x, y = generate_point(game_size)
        game_area[x][y] = 1


def is_game_finished(game_area):
    game_finished = True
    for row in game_area:
        for ship in row:
            if ship:
                game_finished = False
                break

    return game_finished

def hit_boat(game_area, x, y):
    if game_area[x][y]:
        game_area[x][y] = 0
        print("You hit something")
        return ("HIT", x, y)
    else:
        print("You missed")
        return ("MISSED", x, y)

# def update_game_field(game_field, list_of_taken_shots):

def split_user_input(user_input):
    user_input = user_input.split(",")
    x = int(user_input[0]) - 1
    y = int(user_input[1]) - 1
    return [x, y]




game_size = int(input("Enter game size(5-15): "))

while not game_size in range(5, 16):
    print("The game size is outside of expected range.")
    game_size = int(input("Enter game size(5-15): "))
    if game_size in range(5, 16):
        break

game_area = generate_field(game_size, 0)

generate_point_ships(game_area, game_size)

game_field = generate_field(game_size, "Unknown")
print(np.matrix(game_field))
list_of_taken_shots = []

while not is_game_finished(game_area):
    print(np.matrix(game_field))
    user_input = input("Enter x and y values to target(10, 10) or Q to quit game: ")
    if user_input == 'Q':
        print("You quit the game.")
        break

    coordinates = split_user_input(user_input)
    if not (1 <= coordinates[0] <= game_size and 1 <= coordinates[1] <= game_size):
        print("The coordinates are out of expected range")
    else:
        result_of_shot = hit_boat(game_area, coordinates[0], coordinates[1])
        list_of_taken_shots.append(result_of_shot)
        for list in list_of_taken_shots:
            if list[0] == "MISSED":
                game_field[list[1]][list[2]] = "O"
            if list[0] == "HIT":
                game_field[list[1]][list[2]] = "X"

if user_input != "Q":
    print("Congratulations! You sunk all the ships and won.")
