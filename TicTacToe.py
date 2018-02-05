# Make a game of tictactoe
# need to...
# draw the board each time
# each spot on the board is part of a list
# user inputs like pc numpad 789 456 123 top to bottom
# player X and player O
# Check for victory and fail conditions

# initialize our board variable
board = []
for i in range(0,10):
    board.append(' ')

# function for printing the board
def printBoard():
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-+-+-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-+-+-")
    print(board[1] + '|' + board[2] + '|' + board[3])

printBoard()