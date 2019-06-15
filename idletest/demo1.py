guess = int(input('Guess a number between 1 and 100:  '))
tries = 1
num = 20
while guess != num:
    if guess > num:
        print("That guess is too high, try a smaller number")
        guess = int(input('Guess another number: '))
        tries += 1
    elif guess < num:
        print("That guess is too low, try a larger number")
        guess = int(input('Guess another number: '))
        tries += 1


if tries == 1:
    print("Hey you got it in one try")
else:
    print("hey, you got it in ",  tries , "tries")
