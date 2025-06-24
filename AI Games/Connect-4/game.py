import math
import random  # random is used to randomly pick a starting player

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER = 0   # This represents the human player. We assign the number 0 as a label for the player.
AI = 1
EMPTY = 0     # This defines the value for an empty cell on the board. A cell with 0 means it's empty and available for a move.
PLAYER_PIECE = 1
AI_PIECE = 2
WINDOW_LENGTH = 4
DEPTH = 4  # Minimax depth   #  This defines how many moves ahead the AI will think using the minimax algorithm. A deeper depth means smarter AI but slower performance.

def create_board():
    return [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

def print_board(board):
    print("\n".join(str(row) for row in board[::-1]))  # Prints the board in reverse (bottom row shown at the bottom)

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0  # Checks if the top of the column is empty (so a move can be made).

def get_next_open_row(board, col): # Finds the lowest empty row in a column
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
    return None

def drop_piece(board, row, col, piece):  #  Drops the player's or AI’s piece into the board
    
    board[row][col] = piece

def winning_move(board, piece):  # Checks for 4-in-a-row horizontally, vertically, or diagonally for the given player.
    # Check horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Check positively sloped diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    # Check negatively sloped diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    return False

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 5

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 8

    return score

def score_position(board, piece):
    score = 0
    # Center column preference
    center_array = [board[r][COLUMN_COUNT // 2] for r in range(ROW_COUNT)]  # This gives more weight to the middle column (column 3 in a 0–6 grid).
    score += center_array.count(piece) * 6  # প্রতিটা নিজের piece এর জন্য 6 স্কোর যোগ হয়।

    # Horizontal score
    for r in range(ROW_COUNT):       # Take every set of 4 consecutive cells.
        row_array = [board[r][c] for c in range(COLUMN_COUNT)]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Vertical score
    for c in range(COLUMN_COUNT):
        col_array = [board[r][c] for r in range(ROW_COUNT)]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Positive sloped diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    # Negative sloped diagonal
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r - i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score

def get_valid_locations(board):  # Returns a list of columns where a move is possible.
    return [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]

def is_terminal_node(board):  # Checks if the game is over either by win or draw
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingPlayer):  #  Recursive minimax function with alpha-beta pruning to choose the best move for the AI.
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -100000)
            else:
                return (None, 0)
        return (None, score_position(board, AI_PIECE))

    if maximizingPlayer:
        value = -math.inf   # Start with the worst possible score for maximizer (AI).
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)  # Simulate the move: make a copy of the board, drop a chip in the current column for AI.
            temp_board = [r[:] for r in board]   # r[:] creates a copy of the list r
            drop_piece(temp_board, row, col, AI_PIECE)
            _, new_score = minimax(temp_board, depth - 1, alpha, beta, False)  # minimax recursively for the next player (Player's move).
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = [r[:] for r in board]
            drop_piece(temp_board, row, col, PLAYER_PIECE)
            _, new_score = minimax(temp_board, depth - 1, alpha, beta, True)
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value

# ---- Main Game Loop ----
board = create_board() #  Initializes game, creates board, randomly chooses who plays first.
game_over = False
print_board(board)

turn = random.randint(PLAYER, AI)

while not game_over:
    if turn == PLAYER:
        print("Your move:")
        col = int(input("Enter column (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, PLAYER_PIECE)
            if winning_move(board, PLAYER_PIECE):
                print_board(board)
                print("You win!")
                game_over = True
            turn = AI
    else:
        print("AI is thinking...")
        col, _ = minimax(board, DEPTH, -math.inf, math.inf, True)
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)
            print(f"AI placed at column {col}")
            if winning_move(board, AI_PIECE):
                print_board(board)
                print("AI wins!")
                game_over = True
            turn = PLAYER

    print_board(board)
    if len(get_valid_locations(board)) == 0 and not game_over:
        print("It's a draw!")
        break
    
    
    
    
    
    
    
    
    # AI কোন চাল সবচেয়ে ভালো হবে সেটা নির্ধারণের জন্য minimax অ্যালগরিদম ব্যবহার করা হয়েছে।
    # এখানে alpha-beta pruning ব্যবহার হয়েছে সময় বাঁচানোর জন্য।
    
    #board[::-1] is a Python list slicing technique.
    # It reverses the order of the rows in the board.
    
    # | Syntax        | Meaning                               
    # [::-1]`      | Reverse the list                      
    # board[::-1]` | Show board from top to bottom (for UI
    
    
    #| Code Part      | Meaning in English                    | বাংলা অর্থ               |
    #| -------------- | ------------------------------------- | ------------------------ |
    #| `c:c + 4`      | Slice 4 horizontal items from col `c` | ডানে ৪টা ঘর              |
    #| `r:r + 4`      | Slice 4 vertical items from row `r`   | নিচে ৪টা ঘর              |
    #| `r + i, c + i` | Diagonal down-right (↘)              | নিচে ও ডানে একসাথে যাওয়া |
    #| `r - i, c + i` | Diagonal up-right (↗)                | উপরে ও ডানে একসাথে যাওয়া |
    
    
    
    
   # _, is a placeholder variable in Python.
   #It means: “I don’t care about this value.”
   #In this line, minimax() returns two values (e.g., best_col, score), but you only want score, so you ignore the first one using _.


