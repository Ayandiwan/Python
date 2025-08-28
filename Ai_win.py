import random

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(row)
    print()

def is_winner(board, player):
    # Rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def ai_move(board):
    empty_cells = get_empty_cells(board)

    # 1. Can AI win this turn?
    for row, col in empty_cells:
        board[row][col] = 'O'
        if is_winner(board, 'O'):
            return
        board[row][col] = ' '

    # 2. Can AI block player's win?
    for row, col in empty_cells:
        board[row][col] = 'X'
        if is_winner(board, 'X'):
            board[row][col] = 'O'
            return
        board[row][col] = ' '

    # 3. Take center if free
    if board[1][1] == ' ':
        board[1][1] = 'O'
        return

    # 4. Take a corner if free
    for row, col in [(0,0), (0,2), (2,0), (2,2)]:
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return

    # 5. Random move
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'

def main():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe! You are X. AI is O.")

    while True:
        print_board(board)

        # Player move
        try:
            move = input("Enter your move as row and column (0 0 to 2 2): ")
            i, j = map(int, move.strip().split())
            if board[i][j] != ' ':
                print("Cell already taken. Try again.")
                continue
            board[i][j] = 'X'
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
            continue

        if is_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move(board)

        if is_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
