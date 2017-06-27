from sys import exit

def gold_room():
    print("how much god u wnat?")

    choice=input(">")
    if "0" in choice or "1" in choice:
        how_much=int(choice)
    else:
        dead("Man, Type num")

    if how_much<50:
        print("not greedy= win")
        exit(0)
    else:
        dead("GREED!")

def bear_room():
    print("bear in fron door. move bear?")
    bear_moved = False

    while True:
        choice = input(">")

        if choice=="take honey":
            dead("bear kills")
        elif choice== "taunt bear" and not bear_moved:
            print("go door")
            bear_moved=True
        elif choice == "taunt bear" and bear_moved:
            dead("u die")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("no idea")

def cthulu_room():
    print("flee or head")
    choice = input(">")

    if "flee"  in choice:
        start()
    elif "head" in choice:
        dead("tasty")
    else:
        cthulu_room()

def dead(why):
    print(why,"nice")
    exit(0)

def start():
    print("left or right")

    choice=input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("die")

start()
