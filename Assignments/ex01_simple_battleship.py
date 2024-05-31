"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730449145"

boat_location_string: str = input("Pick a secret boat location between 1 and 4:")
boat_location: int = int(boat_location_string)

if (boat_location) > 4:
    print(f"Error! {boat_location} too high!")
    exit()
if (boat_location) < 1:
    print(f"Error! {boat_location} too low!")
    exit()

guess_1_string: str = input("Guess a number between 1 and 4:")
guess_1: int = int(guess_1_string)

if (guess_1) > 4:
    print("Error! [guess_1] too high!")
    exit()
if (guess_1) < 1:
    print("Error! [guess_1] too low!")
    exit()

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""

if guess_1 == boat_location:
    result = RED_BOX
if guess_1 != boat_location:
    result = WHITE_BOX
 
if guess_1 == 1:
    print(result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if guess_1 == 2:
    print(BLUE_BOX + result + BLUE_BOX + BLUE_BOX)
if guess_1 == 3:
    print(BLUE_BOX + BLUE_BOX + result + BLUE_BOX)
if guess_1 == 4:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + result)

if guess_1 == boat_location:
    result = RED_BOX
    print("Correct! You hit the ship!")
else:
    result = WHITE_BOX
    print("Incorrect! You missed the ship.")