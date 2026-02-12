import random

# Simple Tic Tac Toe game in Python
# The game board is represented as a 2D list, and players take turns to input their moves.
# The game checks for a winner after each move and also checks for a draw if the board is full without any winner.
# check_winner(board, player) checks if the current player has won by checking all rows, columns, and diagonals for three of the same symbol.
# The is_draw(board) function checks if all cells are filled without any winner, indicating a draw. 
# The tic_tac_toe() function manages the game flow, alternating turns between players and handling user input.


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)



def check_winner(board, player):                                               #Check if the current player has won
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_draw(board):                                                             #Check if the board is full without any winner, indicating a draw
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():                                                              #Main function to run the game, alternating turns between players and handling user input
    board = [[" " for _ in range(3)] for _ in range(3)]                         #Initialize the game board as a 3x3 grid filled with spaces
    players = ["O", "X"]                                                        #Define the two players, O and X
    current_player = random.choice(players)                                     #Randomly select which player goes first
    
    while True:                                                                 #Start the game loop, which continues until there is a winner or a draw
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        try:                                                                    #Get user input for row and column, ensuring that the input is valid and the chosen cell is not already occupied
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] != " ":
                print("Cell already occupied. Try again.")
                continue
            board[row][col] = current_player
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"
        
           
tic_tac_toe()


