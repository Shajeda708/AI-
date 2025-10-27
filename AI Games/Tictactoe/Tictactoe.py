import tkinter as tk

# Initialize the game window
window = tk.Tk()
window.title("Tic Tac Toe (Minimax AI)")
window.resizable(False, False)

# Create the board (3x3)
board = [" " for _ in range(9)]

# Player and AI symbols
PLAYER = "X"
AI = "O"

# Winning combinations
winning_combos = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]

# Function to check for a winner or a tie on the board
def check_winner(b):
    for (x, y, z) in winning_combos:
        if b[x] == b[y] == b[z] and b[x] != " ":
            return b[x]
    if " " not in b:
        return "Tie"
    return None

# Minimax algorithm to choose the best possible AI move
def minimax(b, is_maximizing):
    result = check_winner(b)
    if result == AI:
        return 1
    elif result == PLAYER:
        return -1
    elif result == "Tie":
        return 0

    if is_maximizing:
        # AI's turn (maximize score)
        best_score = -999
        for i in range(9):
            if b[i] == " ":
                b[i] = AI
                score = minimax(b, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 999
        # Player's turn (minimize score)
        for i in range(9):
            if b[i] == " ":
                b[i] = PLAYER
                score = minimax(b, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -999  
    move = None
    # Try all possible moves and choose the best one
    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    # Make the best move           
    if move is not None:
        board[move] = AI
        buttons[move].config(text=AI, fg="red", state="disabled")

    # Check game result after AI move    
    winner = check_winner(board)
    if winner:
        game_over(winner)

# Handle player's move
def player_move(i):
    if board[i] == " ":
        board[i] = PLAYER
        buttons[i].config(text=PLAYER, fg="blue", state="disabled")

        # Check for winner after player's move
        winner = check_winner(board)
        if winner:
            game_over(winner)
            return
        
        ai_move()  # If no winner, let AI play

# Display winner on window and reset option
def game_over(winner):
    if winner == "Tie":
        result_label.config(text="It's a Tie!")
    elif winner == PLAYER:
        result_label.config(text="You Win!")
    else:
        result_label.config(text="AI Wins!")
    for btn in buttons:
        btn.config(state="disabled")

# Reset the board
def reset_board():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ", state="normal")
    result_label.config(text="")

# Create 3x3 grid of buttons
buttons = []
for i in range(9):
    btn = tk.Button(window, text=" ", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: player_move(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Label to display results
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# reset button 
reset_button = tk.Button(window, text="Reset", font=("Arial", 12), command=reset_board)
reset_button.grid(row=4, column=0, columnspan=3, pady=5)

# Start the GUI loop
window.mainloop()
