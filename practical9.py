import math

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check for draw
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Evaluation function
def evaluate(board):
    if check_win(board, 'X'):
        return +1
    elif check_win(board, 'O'):
        return -1
    else:
        return 0

# Minimax function
def minimax(board, depth, isMax):
    score = evaluate(board)

    # Terminal states
    if score == 1:
        return score
    if score == -1:
        return score
    if is_draw(board):
        return 0

    if isMax:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best

# Function to find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Main Function
def main():
    board = [
        ['X', 'O', 'X'],
        ['O', 'O', ' '],
        [' ', 'X', ' ']
    ]

    print("Current Board:")
    print_board(board)

    best_move = find_best_move(board)
    print(f"\nThe Optimal Move is : Row = {best_move[0]}, Column = {best_move[1]}")

    board[best_move[0]][best_move[1]] = 'X'
    print("\nBoard After AI Move:")
    print_board(board)

if __name__ == "__main__":
    main()
