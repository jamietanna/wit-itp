from pyzork_helper import *

def start():
    print "You wake up in the Business School at the University of Nottingham"
    print "You look around and see the lecture theatre all around you"

    while True:
        print ""
        print "Go for a 'nap'"
        print "Try and 'exit'"
        inp = get_input_from_user("What will you do?")

        if inp == "nap":
            print "You go for a nap, and wake up again not long after"
        elif inp == "exit":
            print "You find yourself on the stairs, and follow them down to the main lobby"
            lobby()

def lobby():
    print "..."
    print "..."

    while True:
        print ""
        print "..."
        inp = get_input_from_user("What will you do?")

start()
