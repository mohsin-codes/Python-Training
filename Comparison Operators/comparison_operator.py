temp = int(input("What's the temperature like? "))

if temp >= 30:
    print("It is a hot day")
elif temp <= 10:
    print("It is a cold day")
elif temp == 20:
    print("It is a beautiful day")
else:
    print("It is neither a hot nor a cold day")