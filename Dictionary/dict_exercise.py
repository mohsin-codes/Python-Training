numbers = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}

output = ""
user_num = input("Phone Number: ") 
for i in user_num:
    output += numbers.get(i, "!") + " "
print(output)