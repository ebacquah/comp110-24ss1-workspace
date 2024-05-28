"""Number guessing game"""
CORRECT: int = 8 
my_number_string: str=input("Guess a number")
my_number :int =int(my_number_string)
while my_number != CORRECT:
    if my_number % 2 == 0: 
        print("Even")
    else:
        print("Odd")
    my_number_string = input("Guess again:")
    my_number = int (my_number_string)



