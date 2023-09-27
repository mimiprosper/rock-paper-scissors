# Rock-Paper-Scissor Game Use Cases :

''' 1. Rock & Paper --> Paper Wins
    2. Paper & Scissor --> Scissor Wins
    3. Scissor & Rock --> Rock Wins
    4. Rock & Rock --> Tie
    5. Paper & Paper --> Tie
    6. Scissor & Scissor --> Tie 
    7. Paper & Rock --> Paper Wins
    8. Scissor & Paper --> Scissor Wins
    9. Rock & Scissor --> Rock Wins 
'''


import random

r = 'rock'
p = 'paper'
s = 'scissor'

while True:

    me = input("(Play r = rock, p = paper, s = scissor, e = exit) I select: ").lower()
    computer = random.choice(['r', 'p', 's'])
    print('computer selected ', computer)

    if me == 'r' and computer == 'p':
        print('computer won - Paper')
    elif me == 'p' and computer == 'r':
        print('I won - Paper')
    elif me == 'p' and computer == 's':
        print('computer won - Scissor')
    elif me == 's' and computer == 'p':
        print('I won - Scissor')
    elif me == 's' and computer == 'r':
        print('computer won - Rock')
    elif me == 'r' and computer == 's':
        print('I won - Rock')
    elif me == "s" and computer == 's':
        print("Tie !!!")
    elif me == "p" and computer == 'p':
        print("Tie !!!")
    elif me == "r" and computer == 'r':
        print("Tie !!!")
    elif me == 'e':
        print("You have exited the game, Good bye!!!")
        exit()
    else:
        print('You made a wrong selection')

