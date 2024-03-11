"""
Program: Connect Four Game
Author:
    Name: Momen Abd El-Kader Abd El-Naby Abd El-Kader
    ID: 20230432
    Section: Not assigned yet.
Version: 1.0
Date: 1 March 2024
"""
# Declare global variables
rows = 6
columns = 7


def main():
    # Display game name and initialize board as 6x7 list of lists
    print("                  ========================== Connect 4 ========================== \n")
    board = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""]
            ]
    print_board(board)
    print("How to play: enter a column number that you want to drop your symbol in \n")

    # Game Loop
    while True:
        # Player 1's Loop
        move = input("Player X's Turn: ")
        while True:
            # Validate column number
            if not valid_move(move):
                move = input("Invalid! Please enter a number between 1 and 7: ")
                continue
            # Validate the column itself
            elif not valid_column(board, int(move) - 1):
                move = input("Invalid! Please drop the symbol into a column that's not full: ")
                continue
            else:
                execute_turn(board, int(move) - 1, 'X')
                print_board(board)
                check_for_winner(board, 'X')
                break

        # Player 2's Loop
        move = input("Player O's Turn: ")
        while True:
            # Validate column number
            if not valid_move(move):
                move = input("Invalid! Please enter a number between 1 and 7: ")
                continue
            # Validate the column itself
            elif not valid_column(board, int(move) - 1):
                move = input("Invalid! Please drop the symbol into a column that's not full: ")
                continue
            else:
                execute_turn(board, int(move) - 1, 'O')
                print_board(board)
                check_for_winner(board, 'O')
                break


# Draw the board to visualize the game (I wish I knew GUI basics)
def print_board(board):
    for row in range(rows):
        print("\n+---+---+---+---+---+---+---+")
        print("|", end="")
        for col in range(columns):
            if board[row][col] == "X":
                print("", board[row][col], end=" |")
            elif board[row][col] == "O":
                print("", board[row][col], end=" |")
            else:
                print("  ", end=" |")
    print("\n+---+---+---+---+---+---+---+")
    print("  1   2   3   4   5   6   7\n")


# Validate player's move
def valid_move(move):
    valid = ["1", "2", "3", "4", "5", "6", "7"]
    if move not in valid:
        return False
    return True


# Check if the column is full (if you find any empty cell then it's valid)
def valid_column(board, move):
    for row in range(rows):
        if not board[row][int(move)]:
            return True
    return False


# Change board according to player's move
def execute_turn(board, move, symbol):
    for cell in range(rows - 1, -1, -1):
        if not board[cell][move]:
            board[cell][move] = symbol
            return


# Check for a winner
def check_for_winner(board, symbol):
    # Check vertical winning condition
    for row in range(rows - 3):
        for col in range(columns):
            if board[row][col] == symbol and board[row + 1][col] == symbol and board[row + 2][col] == symbol and board[row + 3][col] == symbol:
                print(f"\n ************************ Player {symbol} wins ! ************************ \n")
                exit()

    # Check horizontal winning condition
    for row in range(rows):
        for col in range(columns - 3):
            if board[row][col] == symbol and board[row][col + 1] == symbol and board[row][col + 2] == symbol and board[row][col + 3] == symbol:
                print(f"\n ************************ Player {symbol} wins ! ************************ \n")
                exit()

    # Check for Diagonal winning condition (-ve slope)
    for row in range(rows - 3):
        for col in range(columns - 3):
            if board[row][col] == symbol and board[row + 1][col + 1] == symbol and board[row + 2][col + 2] == symbol and board[row + 3][col + 3] == symbol:
                print(f"\n ************************ Player {symbol} wins ! ************************ \n")
                exit()

    # Check for Diagonal winning condition (+ve slope)
    for row in range(3, rows):
        for col in range(columns - 3):
            if board[row][col] == symbol and board[row - 1][col + 1] == symbol and board[row - 2][col + 2] == symbol and board[row - 3][col + 3] == symbol:
                print(f"\n ************************ Player {symbol} wins ! ************************ \n")
                exit()


main()
