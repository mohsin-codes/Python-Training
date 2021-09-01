weight = int(input("What is your weight : "))
unit = input("(L)bs or (K)g : ")

if unit.upper() == "L":
    cWeight = weight / 2.205
    print(f"You are {cWeight} Kilos")
else:
    cWeight = weight * 2.205
    print(f"You are {cWeight} Pounds")