import random


def generate_battleship_area(game_size):
    game_area = [[False for x in range(game_size)] for y in range(game_size)]
    return game_area


def generate_point(game_size):
    x = random.randrange(0, game_size)
    y = random.randrange(0, game_size)

    return x, y

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
        game_area[x][y] = False
        print("You hit something!")
    else:
        print("False alarm.")
def generate_ships(game_area, game_size):
    tons = int(( game_size * game_size ) * 0.2)
    for x in range(tons):
        x, y = generate_point(game_size)
        game_area[x][y] = True


game_size = int(input("Enter game size (1 - 20): "))
game_area = generate_battleship_area(game_size)
generate_ships(game_area, game_size)

while not is_game_finished(game_area):
    user_data = input("Enter X, Y to target: (10,10) or Q to quit game: ")
    if user_data == "Q":
        break
    user_data = user_data.split(",")
    x = int(user_data[0]) - 1
    y = int(user_data[1]) - 1
    # If field size = 10, 11, 11
    # TODO: Add move validator!
    # TODO: Print out of game
    # TODO: 1 vs computer?
    # O O O F ?
    # O O F F ?
    # ...
    hit_boat(game_area, x, y)
    print(game_area)

# X, Y: 3,3
# Size: 1, 3, 5
#
