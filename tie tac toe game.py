import random
# give global variables first
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
currentplayer = "O"
winner = None
gameRunning = True

# printing board
def createboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# take input
def playerinput(board):
    inp = int(input("Enter a number between 1 to 9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "_":
        board[inp - 1] = currentplayer
    else:
        print("A player is already there")

# check horizontal
def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "_":
        winner = board[6]
        return True

# check vertical
def checkvertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[6] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[8] != "_":
        winner = board[2]
        return True

# check diagonals
def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "_":
        winner = board[4]
        return True

# check for a tie
def checktie(board):
    global gameRunning
    if "_" not in board:
        createboard(board)
        print("It's a tie!!")
        gameRunning = False

# switch player
def switch_a_player():
    global currentplayer
    if currentplayer == "O":
        currentplayer = "X"
    else:
        currentplayer = "O"

# computer
def computer(board):
    while currentplayer == "X":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            switch_a_player()

# check win or tie
def checkwin():
    if checkdiagonal(board) or checkhorizontal(board) or checkvertical(board):
        return True

# In the game:
while gameRunning:
    createboard(board)
    playerinput(board)
    if checkwin():
        createboard(board)
        print(f"The winner is {winner} ")
        break 
    # Exit the loop if there's a winner
    checktie(board)
    switch_a_player()