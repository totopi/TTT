# Make a game of tictactoe
# need to...
# draw the board each time
# each spot on the board is part of a list
# user inputs like pc numpad 789 456 123 top to bottom
# player X and player O
# Check for victory and fail conditions

# import stuff
import msvcrt

# initialize our board variable
board = []
for i in range(0,10):
    board.append(' ')

# function for printing the board
def printBoard():
    print()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-+-+-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-+-+-")
    print(board[1] + '|' + board[2] + '|' + board[3])
    print()

printBoard()
print("Welcome to Tic-Tac-Toe!")
print("Please input your board position like a pc numpad, not a phone.")
# now for THE GAME
for turnCount in range(1, 10):


    # ODD TURNS = X
    if(turnCount % 2 == 1):
        x = 0
        while x not in range (1, 10):
            print("Please input an integer from 1-9")
            x = int(input("Player X, where would you like to go: "))
            if board[x] != ' ':
                print("\nSorry, that space is already occupied by a '" + board[x] + "'")
                print("Please try again")
                msvcrt.getch()
                printBoard()
                x = 0
        board[x] = 'X'
            

    # EVEN TURNS = O
    elif(turnCount % 2 == 0):
        o = 0
        while o not in range (1, 10):
            print("Please input an integer from 1-9")
            o = int(input("Player O, where would you like to go: "))
            if board[o] != ' ':
                print("\nSorry, that space is already occupied by a '" + board[o] + "'")
                print("Please try again")
                msvcrt.getch()
                printBoard()
                o = 0
        board[o] = 'O'    
    turnCount += 1

    printBoard()