from sys import exit

def get_input_from_user(prompt):
    user_input = raw_input(prompt + ": ")
    user_input = str(user_input)
    return user_input

def dead(why):
    print "You died...", why
    exit(0)

def zombies():
    dead("You got eaten by zombies")
