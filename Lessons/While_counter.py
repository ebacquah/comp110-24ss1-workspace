message: str= "Banana"
idx: int = 0
a_counter: int = 0
while idx <len (message):
    print(message[idx])
    if message [idx]== "a":
        a_counter += 1
    idx += 1
print(f"The letter a shows up {a_counter} times")
print("The letter a shows up" + str(a_counter))