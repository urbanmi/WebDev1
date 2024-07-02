km_to_miles_conversionRate = 0.621371192

miles_to_km_conversionRate = 1.609344


toContinue = "Y"

print("Hello User! I am a program that converts kilometres to miles and backwards.")

while toContinue == "Y":

    convertee = input("What would you like to convert?: ")

    if convertee == "kilometres":
        kilometres = int(input("How many kilometres to convert?: "))
        miles = kilometres * km_to_miles_conversionRate
        print(miles, "miles")

    if convertee == "miles":
        miles = int(input("How many miles to convert?: "))
        kilometres = miles * miles_to_km_conversionRate
        print(kilometres, "kilometres")

    else:
        print("I do not recognize this unit.")

    toContinue = input("Would you like to convert anything else? (Y/N): ")
    if toContinue == "N":
            print("Thank You and Goodbye")

    else:
        toContinue = "Y"



