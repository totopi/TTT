# Make a game of tictactoe
# need to...
# draw the board each time
# each spot on the board is part of a list
# user inputs like pc numpad 789 456 123 top to bottom
# player X and player O
# Check for victory and fail conditions

# import msvcrt to allow me to do a wait for any keypress thing
import msvcrt

# initialize our board variable
board = ['','1','2','3','4','5','6','7','8','9']

# function for printing the board
def printBoard():
    print()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-+-+-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-+-+-")
    print(board[1] + '|' + board[2] + '|' + board[3])
    print()

# print this handy dandy starter board with numbers for each position to show how to play
printBoard()

# and now make it empty for when the game is being played shortly
board = []
for i in range(0,10):
    board.append(' ')

# greet the users
print("Welcome to Tic-Tac-Toe!")
print("Please input your desired board position as above.")

# now for THE GAME
for turnCount in range(1, 10):
    
    # ODD TURNS = X
    if(turnCount % 2 == 1):
        # initialize this so the next loop can run
        x = 0

        # go until input is 1-9
        while x not in range (1, 10):

            # get input
            x = int(input("Player X, where would you like to go: "))

            # if it's too small or too big, let user know, wait for them to press something, and print the board
            if ((x < 1) or (x > 9)):
                print("\nSorry, that isn't a valid integer.  Please use 1-9.")
                print("Please try again\n")
                msvcrt.getch()

            # or if someone's already played in that spot, let user know etc
            if board[x] != ' ':
                print("\nSorry, that space is already occupied by a '" + board[x] + "'")
                print("Please try again")
                msvcrt.getch()
                printBoard()
                # x needs to be outside of 1-9 range so the loop will run
                x = 0
        
        # input is good and valid and not taken 
        board[x] = 'X'
    
    # EVEN TURNS = O, copy pasted from above if and replaced xs with os
    elif(turnCount % 2 == 0):
        o = 0
        while o not in range (1, 10):
            o = int(input("Player O, where would you like to go: "))
            if ((o < 1) or (o > 9)):
                print("\nSorry, that isn't a valid integer.  Please use 1-9.")
                print("Please try again\n")
                msvcrt.getch()
            
            if board[o] != ' ':
                print("\nSorry, that space is already occupied by a '" + board[o] + "'")
                print("Please try again")
                msvcrt.getch()
                printBoard()
                o = 0
        board[o] = 'O'
    printBoard()

    # check for winner
    if((board[7] != ' ') and ((board[7] == board[8] == board[9]) or (board[7] == board[4] == board[1]))):
        print("Congratulations, a winner is Player " + board[7] + "!!!")
        break
    elif((board[9] != ' ') and (board[9] == board[6] == board[3])):
        print("Congratulations, a winner is Player " + board[9] + "!!!")
        break
    elif((board[1] != ' ') and (board[1] == board[2] == board[3])):
        print("Congratulations, a winner is Player " + board[1] + "!!!")
        break
    elif((board[5] != ' ') and ((board[4] == board[5] == board[6]) or (board[8] == board[5] == board[2]) or\
         (board[7] == board[5] == board[3]) or (board[1] == board[5] == board[9]))):
        print("Congratulations, a winner is Player " + board[5] + "!!!")
        break