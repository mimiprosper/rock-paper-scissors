# Rock-Paper-Scissor Game Use Cases :

# 1. Rock & Paper --> Paper Wins 
# 2. Paper & Scissor --> Scissor Wins
# 3. Scissor & Rock --> Rock Wins 
# 4. Rock & Rock --> Tie
# 5. Paper & Paper --> Tie
# 6. Scissor & Scissor --> Tie
# 7. Paper & Rock --> Paper Wins 
# 8. Scissor & Paper --> Scissor Wins
# 9. Rock & Scissor --> Rock Wins

r = 'rock'
p = 'paper'
s = 'scissor'
x = 1

while x == 1:

    player1 = input("select: r = rock, p = paper, s = scissor, e = exit : ").lower()
    player2 = input("select: r = rock, p = paper, s = scissor, e = exit : ").lower()

    if player1 == 'r' and player2 == 'p':
        print('player2 won - Paper')
    elif player1 == 'p' and player2 == 'r':
        print("player1 won - Paper")   
    elif player1 == 'p' and player2 == 's':
        print('player2 won - Scissor')
    elif player1 == 's' and player2 == 'p':
        print('player1 won - Scissor')
    elif player1 == 's' and player2 == 'r':
        print('player2 won - Rock')
    elif player1 == 'r' and player2 == 's':
        print('player1 won - Rock')
    elif player1 == 's' and player2 == 's':
        print("Tie !!!")
    elif player1 == 'p' and player2 == 'p':
        print("Tie !!!")
    elif player1 == 'r' and player2 == 'r':
        print("Tie !!!")
    elif player1 == 'e' and player2 == 'e':
        exit() 
    else:
        print('Wrong selection')