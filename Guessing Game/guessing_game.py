secret_number = 9
i = 1
while i<=3:
    guess_number = int(input("Guess a number between 1 to 10: "))
    i = i + 1
    if guess_number == secret_number:
        print("You won")
        break
else:
    print("You Lose")   