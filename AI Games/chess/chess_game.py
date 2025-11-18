import tkinter as tk
from tkinter import simpledialog, messagebox
import chess
import math

AI_DEPTH = 2                     # Depth limit for AI search (higher = smarter but slower)
SQUARE_SIZE = 72                 # Each chess square size in pixels
SELECT_COLOR = "#FFD54F"         # Highlight for selected square
LEGAL_MOVE_COLOR = "#90CAF9"     # Highlight for legal move destinations
LIGHT_COLOR = "#F0D9B5"          # Light squares color
DARK_COLOR = "#B58863"           # Dark squares color
FONT_FAMILY = "Segoe UI Symbol"  # Font for Unicode chess pieces
FONT_SIZE = 40                   # Piece display size

# Piece value table for evaluation
piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

# BOARD EVALUATION FUNCTIONS

def evaluate_board(board):
    """Return a simple material-based evaluation of the board."""
    score = 0
    for piece_type, value in piece_values.items():
        score += value * len(board.pieces(piece_type, chess.BLACK))  # Black’s material
        score -= value * len(board.pieces(piece_type, chess.WHITE))  # Subtract White’s material
    return score


def evaluate_terminal(board, depth):
    """Evaluate endgame situations: checkmate, stalemate, or draw."""
    if board.is_checkmate():
        # If it's checkmate, determine who won
        winner_is_black = (board.turn == chess.WHITE)
        return 100000 - depth if winner_is_black else -100000 + depth
    if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_draw():
        return 0
    return None

# MINIMAX ALGORITHM WITH ALPHA-BETA PRUNING

def minimax(board, depth, alpha, beta, maximizing_player):
    """Perform recursive minimax search with alpha-beta pruning."""
    terminal_score = evaluate_terminal(board, depth)
    if terminal_score is not None:
        return terminal_score
    if depth == 0:
        return evaluate_board(board)

    if maximizing_player:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval_value = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval_value)
            alpha = max(alpha, eval_value)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval_value = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval_value)
            beta = min(beta, eval_value)
            if beta <= alpha:
                break
        return min_eval


def best_move_for_ai(board, depth=AI_DEPTH):
    """Find the best move for AI (Black) using minimax."""
    best_move = None
    best_score = -math.inf
    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth - 1, -math.inf, math.inf, False)
        board.pop()
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# GUI INITIALIZATION

board = chess.Board()
selected_square = None
legal_destinations = []

root = tk.Tk()
root.title("Human vs AI Chess (Minimax AI)")
canvas = tk.Canvas(root, width=8*SQUARE_SIZE, height=8*SQUARE_SIZE, highlightthickness=0)
canvas.pack()
status_lbl = tk.Label(root, text="You: White  —  AI: Black", font=("Arial", 12))
status_lbl.pack(fill="x")

# Unicode chess symbols (white, black)
piece_symbols = {
    chess.PAWN: ('♙', '♟'),
    chess.KNIGHT: ('♘', '♞'),
    chess.BISHOP: ('♗', '♝'),
    chess.ROOK: ('♖', '♜'),
    chess.QUEEN: ('♕', '♛'),
    chess.KING: ('♔', '♚')
}

# HELPER FUNCTIONS

def coord_to_square(x, y):
    """Convert pixel coordinates (click position) to chess square index."""
    col = x // SQUARE_SIZE
    row_from_top = y // SQUARE_SIZE
    row = 7 - row_from_top
    if 0 <= col < 8 and 0 <= row < 8:
        return chess.square(col, row)
    return None


def draw_board():
    """Draw the chess board and all pieces."""
    canvas.delete("all")
    for r in range(8):
        for c in range(8):
            sq = chess.square(c, 7 - r)
            x1, y1 = c * SQUARE_SIZE, r * SQUARE_SIZE
            x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE

            # Determine square color
            color = LIGHT_COLOR if (r + c) % 2 == 0 else DARK_COLOR
            if selected_square == sq:
                color = SELECT_COLOR
            elif sq in legal_destinations:
                color = LEGAL_MOVE_COLOR

            # Draw square
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

            # Draw piece
            piece = board.piece_at(sq)
            if piece:
                symbol = piece_symbols[piece.piece_type][0 if piece.color == chess.WHITE else 1]
                fillcol = "black" if (r + c) % 2 == 0 else "white"
                canvas.create_text(x1 + SQUARE_SIZE // 2, y1 + SQUARE_SIZE // 2,
                                   text=symbol, font=(FONT_FAMILY, FONT_SIZE), fill=fillcol)

    # Draw board labels
    for i, ch in enumerate("abcdefgh"):
        x = i * SQUARE_SIZE + 4
        y = 8 * SQUARE_SIZE - 14
        canvas.create_text(x, y, text=ch, anchor="w", font=("Arial", 9))


def show_result():
    """Display the result when the game ends."""
    res = board.result(claim_draw=True)
    if board.is_checkmate():
        winner = "Black (AI)" if board.turn == chess.WHITE else "White (You)"
        messagebox.showinfo("Game Over", f"Checkmate! Winner: {winner}")
    elif board.is_stalemate():
        messagebox.showinfo("Game Over", "Stalemate — Draw.")
    elif board.is_insufficient_material():
        messagebox.showinfo("Game Over", "Draw — Insufficient material.")
    else:
        messagebox.showinfo("Game Over", f"Game Over: {res}")


def on_click(event):
    """Handle user clicks (selecting and moving pieces)."""
    global selected_square, legal_destinations
    sq = coord_to_square(event.x, event.y)
    if sq is None:
        return

    # If selecting a piece
    if selected_square is None:
        piece = board.piece_at(sq)
        if piece and piece.color == chess.WHITE:
            selected_square = sq
            legal_destinations = [mv.to_square for mv in board.legal_moves if mv.from_square == sq]
            draw_board()
    else:
        mv = None
        sel_piece = board.piece_at(selected_square)

        # Handle pawn promotion
        if sel_piece and sel_piece.piece_type == chess.PAWN and chess.square_rank(sq) in (0, 7):
            promo = simpledialog.askstring("Promotion", "Promote to (q/r/b/n):", parent=root)
            if promo and promo.lower() in ("q", "r", "b", "n"):
                promo_map = {'q': chess.QUEEN, 'r': chess.ROOK, 'b': chess.BISHOP, 'n': chess.KNIGHT}
                mv = chess.Move(selected_square, sq, promotion=promo_map[promo.lower()])
        else:
            mv = chess.Move(selected_square, sq)

        # Execute valid move
        if mv in board.legal_moves:
            board.push(mv)
            selected_square, legal_destinations = None, []
            draw_board()
            root.update_idletasks()

            # Check for end of game
            if board.is_game_over():
                show_result()
                return

            # AI plays after small delay
            root.after(120, do_ai_move)
        else:
            selected_square, legal_destinations = None, []
            draw_board()


def do_ai_move():
    """Let the AI (black) calculate and play its move."""
    global board
    if board.is_game_over():
        show_result()
        return

    mv = best_move_for_ai(board, depth=AI_DEPTH)
    if mv:
        board.push(mv)
        draw_board()
        if board.is_game_over():
            show_result()
    else:
        show_result()

# MAIN EVENT BINDING AND LOOP

canvas.bind("<Button-1>", on_click)
draw_board()
root.mainloop()
