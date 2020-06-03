print("Think of a number between 1 and 100, and I'll guess it.")
print("You have to tell me if my guess is less than, greater than, or equal to your number.")
floor = 1
ceiling = 100
got_it = False 
while not got_it:
    guess = (floor + ceiling) // 2
    print(f"I'm guessing {guess}.")
    result = input("Is my guess less, greater, or equal to your number?")
    result = result.lower()
    result = result[0]
    if result == 'h':
        ceiling = guess - 1
    elif result == 'l':
        floor = guess + 1
    elif result == 'e':
        print("I guessed your number!")
        got_it = True
    else:
        print("I don't know what that means. Try again please.")
​ 