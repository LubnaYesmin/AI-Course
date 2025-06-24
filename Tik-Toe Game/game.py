import math

def print_board(board):
    for row in board:
        print("|".join(row))  # |.join(row) joins the items in each row with a | symbol.
        print("-" * 5)

def check_winner(board):
    # Rows, Columns, and Diagonals
    lines = board + [list(col) for col in zip(*board)] + [     # Combines all possible winning lines: rows, columns, and diagonals
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)]
    ]
    for line in lines:  # range
        if line.count('X') == 3:
            return 'X'
        elif line.count('O') == 3:
            return 'O'
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)  # Returns True if no cell is empty (' ')

def minimax(board, depth, is_maximizing):       # This is the main AI function using the Minimax algorithm.
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf            # If it’s AI’s turn, start with the lowest possible score
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':   # Check each empty cell
                    board[i][j] = 'O'    # Simulate a move, calculate score recursively, undo the move, keep best score.
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score # Returns the best score for AI.
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # Simulate human move, try to minimize AI’s score.
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf   # Starts with worst score and invalid move.
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':  # Check all empty spots
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:  # Simulates the move, gets score, keeps the best move
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter your move row (0-2): "))
                col = int(input("Enter your move column (0-2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("That spot is taken. Try again.")
            except (IndexError, ValueError):
                print("Invalid input. Try again.")

        print_board(board)

        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        row, col = best_move(board)
        board[row][col] = 'O'
        print_board(board)

        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#+∞ (positive infinity) means: worst-case for minimizing → so human (minimizer) starts with +∞ to find the lowest score.

#  −∞ (negative infinity) means: worst-case for maximizing → so AI (maximizer) starts with −∞ to find the highest score.