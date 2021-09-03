try:
    age = int(input("Enter your age : "))
    income = 20000
    risk = income/age
    print(age)
    print(risk)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Value should only be of type : int")