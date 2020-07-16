"""This function has a person name as an input and returns a string in the following layout:
This function has a person name as an input and returns a string in the following layout:
Hello <name> and welcome to the World of Games (WoG).
Here you can find many cool games to play."""


def welcome(name):
    return "Hello " + name + " and welcome to the World of Games (WoG)." + '\n' + "Here you can find many cool games " \
                                                                                  "to play. "


"""This function prints out the following text:
Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS"""


def load_game():
    while True:
        try:

            choice = int(input("Please choose a game to play:"
                               "\n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"
                               "\n 2. Guess Game - guess a number and see if you chose like the computer"
                               "\n 3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))

            while choice not in range(1, 4):
                choice = int(input('Please choose a game to play:'
                                   '\n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back'
                                   '\n 2. Guess Game - guess a number and see if you chose like the computer'
                                   '\n 3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'))

            return choice

        except:

            print()


"""Gets an input from the user about the game he chose. After receiving the game number from
the user, the function will get the level of difficulty with the following text and also save to a
variable:
Please choose game difficulty from 1 to 5:
The function will check the input of the chosen game (the input suppose to be a number
between 1 to 3), also will check the input of level of difficulty (input should be a number between
1 to 5)."""


def difficulty():
    diff = (input("Please choose game difficulty from 1 to 5:\n"))

    while (not diff.isdigit()) or (int(diff) not in range(1, 6)):
        if not diff.isdigit():
            diff = (input('Please choose game difficulty from 1 to 5:\n'))
        else:
            diff = (input('Please choose game difficulty from 1 to 5:\n'))

    return diff

"""diff = (input("Please choose game difficulty from 1 to 5:\n"))
while ( not diff.isdigit() ) or ( int(diff) not in range(1, 6) ) :
    if not diff.isdigit():
        diff = (input("u must choose a number: "))
    else:
        diff = (input('Please choose game difficulty from 1 to 5:'))

print(diff)"""
