"""Practice writing functions."""


# defining the function
def my_max(number1: int, number2: int) -> int:  # signatures
    """Return the largest of the two numbers."""
    if number1 >= number2:
        return number1
    else:
        return number2


max: int = my_max(1, 12)
other_max: int = my_max(13, 3)
print(other_max)
