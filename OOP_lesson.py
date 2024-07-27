class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

class basketball_player(Player):
    #atributtes
    def __init__(self, points, rebounds, assists, first_name, last_name, height_cm, weight_kg):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
#method
    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

player_one = basketball_player(first_name="Lebron", last_name="James", height_cm=189, weight_kg=180, points=30, rebounds=20, assists=16)
player_two = basketball_player(first_name="Luka", last_name="Doncic", height_cm=189, weight_kg=180, points=35, rebounds=20, assists=16)
print(player_one.first_name)
print(player_one.last_name)




player_one_lbs_weight = player_one.weight_to_lbs()

print(player_one_lbs_weight)

class footballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


Fplayer_one = footballPlayer(first_name="Ronaldo", last_name="/", height_cm=180, weight_kg=180, goals=3, yellow_cards=2, red_cards=4)
Fplayer_two = footballPlayer(first_name="Lionel", last_name="Messi", height_cm=160, weight_kg=70, goals=2, yellow_cards=2, red_cards=4)


class vehicle():
    def __init__(self, wheels, color, doors, driven_km):
        self.wheels = wheels
        self.color = color
        self.doors = doors
        self.driven_km = driven_km


class auto(vehicle):
    def __init__(self, wheels, color, doors, driven_km, technical_warranty, vinjeta):
        super().__init__(wheels=wheels, color=color, doors=doors, driven_km=driven_km)
        self.technical_warranty = technical_warranty
        self.vinjeta = vinjeta


class Point:
    def __init__(self, data, next_element):
        self.data = data
        self.next_element = next_element



it1 = Point(data=5, next_element=3)
it2 = Point(data=3, next_element=None)

print(it1)
