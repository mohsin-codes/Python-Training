car_command = ""
started = False
while True:
    car_command = input()
    if car_command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started.. Ready to go")
    elif car_command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.. Cannot move now")
    elif car_command == "help":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to exit
        ''')
    elif car_command == "quit":
        break
    else:
        print("I do not understand that..")
else:
    print("Wrong Input.")