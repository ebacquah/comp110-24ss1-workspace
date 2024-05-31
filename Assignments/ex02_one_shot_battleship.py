"""One Shot Battleship"""
__author__ = "730449145"

SIZE_GRID: int = 4
SECRET_ROW: int = 3
SECRET_COLUMN: int = 2

guess_row: int = int(input("Guess a row:"))

while guess_row > SIZE_GRID or guess_row < 1:
    guess_row: int = int(input(f"The grid is only {SIZE_GRID} by {SIZE_GRID}. Try again: "))

guess_column: int = int(input("Guess a column:"))

while guess_column > SIZE_GRID or guess_column < 1:
    guess_column: int = int(input(f"The grid is only {SIZE_GRID} by {SIZE_GRID}. Try again:"))


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""

if guess_row == SECRET_ROW and guess_column == SECRET_COLUMN:
    result = RED_BOX
else:
    result = WHITE_BOX
   
# if guess_column == SECRET_COLUMN:
#     result = RED_BOX
# if guess_column != SECRET_COLUMN:
#     result = WHITE_BOX


# column_counter: int = 1
# while column_counter <= SIZE_GRID:
#     row_result: str =  ""
#     if guess_column  == column_counter:
#         row_result = RED_BOX
#     else:
#         row_result = BLUE_BOX
#     column_counter += 1

# while column_counter <= SIZE_GRID:
#     row_result = BLUE_BOX
#     column_counter += 1

# print (row_result)

row_counter: int = 1
while row_counter <= SIZE_GRID:
    row_result: str =  ""
    column_counter: int = 1
    if guess_row  == row_counter:
        while column_counter <= SIZE_GRID:
            if guess_column  == column_counter:
                row_result += result 
            else:
                row_result += BLUE_BOX    
            column_counter += 1
    else:
        while column_counter <= SIZE_GRID:
            row_result += BLUE_BOX
            column_counter += 1
    print(row_result)
    row_counter += 1


if guess_row == SECRET_ROW and guess_column != SECRET_COLUMN:
    print("Close! Correct row, wrong column.")
elif guess_row != SECRET_ROW and guess_column == SECRET_COLUMN:
    print("Close! Correct column, wrong row.")


if guess_row == SECRET_ROW and guess_column == SECRET_COLUMN:
    print("Hit!")   
elif guess_row != SECRET_ROW and guess_column != SECRET_COLUMN:
    print("Miss!")
