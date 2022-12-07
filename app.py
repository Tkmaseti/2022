command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("You have already started!")
        else:
            started = True
            name = input("What is your name? ")
            surname = input("What is your surname? ")
            sex = input("What is your gender? ")
            if sex == "male":
                print("Hello Mr " + surname)
            elif sex == "female":
                print("Hello Miss " + surname)
            else:
                print("Sorry I don't understand")
    elif command == "stop":
        if not started:
            print("You have already stopped!")
        else:
            started = False
            exits = input("Are you sure you wan to exit? Y/N")
            print(exits)
            if exits == "N":
                print("Press help for more options")
            else:
                break

    elif command == "help":
        print("""
These are the options:

start - to start the game
stop - to stop the game 
quit - to quit the game
        """)
    elif command == "play":
        game = input("Truth or Dare? ")
        if game == "Truth".lower():
            print("Who would you rather make out between th guys you with?")
        elif game == "Dare".lower():
            print("I dare you to kiss the person on your left on the chick.")
        else:
            print("Sorry I don't understand your selection press play to retry")
        break
