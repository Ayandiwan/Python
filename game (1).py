import random

def initialize_board():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return board

def print_board(board):
    for i in board:
        print(i)
        print()

def is_winner(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def get_empty_cells(board):
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty.append((i, j))
    return empty




'''
def ai_move(board):
    
    empty_cells = get_empty_cells(board)
    
    if empty_cells:
        move = random.choice(empty_cells)
        print(move)
        row, col = move
        board[row][col] = "O"
'''

def ai_move(board):
    empty_cells = get_empty_cells(board)

    # Step 1: Can AI win?
    for row, col in empty_cells:
        board[row][col] = 'O'
        if is_winner(board, 'O'):
            return
        board[row][col] = ' '  # Undo move

    # Step 2: Can AI block player from winning?
    for row, col in empty_cells:
        board[row][col] = 'X'
        if is_winner(board, 'X'):
            board[row][col] = 'O'  # Block the player
            return
        board[row][col] = ' '  # Undo move

    # Step 3: Pick center if available
    if board[1][1] == ' ':
        board[1][1] = 'O'
        return

    # Step 4: Pick a random move
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'





def main():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe! You are X. AI is O.")
    
    while True:
        print_board(board)
        
        # Player move
        move = input("Enter your move as row and column (0 0 to 2 2): ")
        i, j = move.strip().split()
        i = int(i)
        j = int(j)
        board[i][j] = "X"  

        if is_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI move
        ai_move(board)

        if is_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
