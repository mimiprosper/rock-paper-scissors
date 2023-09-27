# Game Use Cases :

'''  1. Scissor & Scissor --> Tie 
    2. Paper & Rock --> Paper Wins
    3. Scissor & Paper --> Scissor Wins
    4. Rock & Scissor --> Rock Wins 
    5. Rock & Paper --> Paper Wins
    6. Paper & Scissor --> Scissor Wins
    7. Scissor & Rock --> Rock Wins
    8. Rock & Rock --> Tie
    9. Paper & Paper --> Tie
   
'''


import random
x = 1

while x == 1:

    me = input("(Play rock,  paper, scissor, e = exit) select: ").lower()
    computer = random.choice(['rock', 'paper', 'scissor']).lower()
    print('computer selected ', computer)

    if me == 'rock' and computer == 'paper':
        print('computer won - Paper')
    elif me == 'paper' and computer == 'rock':
        print('I won - Paper')
    elif me == 'paper' and computer == 'scissor':
        print('computer won - Scissor')
    elif me == 'scissor' and computer == 'paper':
        print('I won - Scissor')
    elif me == 'scissor' and computer == 'rock':
        print('computer won - Rock')
    elif me == 'rock' and computer == 'scissor':
        print('I won - Rock')
    elif me == "scissor" and computer == 'scissor':
        print("Draw !!!")
    elif me == "paper" and computer == 'paper':
        print("Draw !!!")
    elif me == "rock" and computer == 'rock':
        print("Draw !!!")
    elif me == 'e':
        print("exit the game!!!")
        exit()
    else:
        print('Wrong selection, try again')
