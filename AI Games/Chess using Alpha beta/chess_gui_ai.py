import pygame  # Used to create the chessboard GUI.
import chess   # From the python-chess library — handles all chess logic.
import sys

# Constants
WIDTH, HEIGHT = 480, 480
SQ_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Piece images dictionary
PIECE_IMAGES = {}

# Load piece images
def load_images(): # Scales them to fit each square.
    pieces = ['P', 'R', 'N', 'B', 'Q', 'K']
    for piece in pieces:
        PIECE_IMAGES['w' + piece] = pygame.transform.scale(pygame.image.load(f"image/w{piece}.png"), (SQ_SIZE, SQ_SIZE))
        PIECE_IMAGES['b' + piece] = pygame.transform.scale(pygame.image.load(f"image/b{piece}.png"), (SQ_SIZE, SQ_SIZE))

# Draw the board
def draw_board(screen, board):
    colors = [WHITE, GRAY]
    for r in range(8):
        for c in range(8):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    draw_pieces(screen, board)

# Draw the pieces on the board
def draw_pieces(screen, board):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)
            piece_str = ('w' if piece.color == chess.WHITE else 'b') + piece.symbol().upper()
            screen.blit(PIECE_IMAGES[piece_str], pygame.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Evaluation function (basic material count)
def evaluate(board):
    values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9
    }
    eval = 0
    for piece in board.piece_map().values():
        value = values.get(piece.piece_type, 0)
        eval += value if piece.color == chess.BLACK else -value  # Positive score means Black is better, negative means White
    return eval

# Alpha-Beta Pruning algorithm
def alpha_beta(board, depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate(board), None

    best_move = None
    if maximizing:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = alpha_beta(board, depth-1, alpha, beta, False)  # alpha_beta(...) returns two values: (score, move)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = alpha_beta(board, depth-1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# Main game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess: You vs AI (Alpha-Beta)")
    board = chess.Board()
    clock = pygame.time.Clock()
    load_images()

    selected_square = None
    running = True

    while running:
        draw_board(screen, board)
        pygame.display.flip()

        if board.turn == chess.BLACK:  # AI's turn
            print("AI is thinking...")
            _, move = alpha_beta(board, 3, -float('inf'), float('inf'), True)
            if move:
                board.push(move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and board.turn == chess.WHITE:
                col = event.pos[0] // SQ_SIZE
                row = 7 - (event.pos[1] // SQ_SIZE)
                square = chess.square(col, row)

                if selected_square is None:
                    if board.piece_at(square) and board.piece_at(square).color == chess.WHITE:
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                    selected_square = None

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
