import tkinter as tk

# ----- Global variables -----
coins = 15  # starting number of coins

# ----- Minimax functions -----
def minimax(coins_left, is_ai_turn):
    if coins_left == 0:
        return -1 if is_ai_turn else 1
    if is_ai_turn:
        best = -999
        for move in range(1, 4):
            if coins_left - move >= 0:
                score = minimax(coins_left - move, False)
                best = max(best, score)
        return best
    else:
        best = 999
        for move in range(1, 4):
            if coins_left - move >= 0:
                score = minimax(coins_left - move, True)
                best = min(best, score)
        return best

def best_move(coins_left):
    best_score = -999
    move_choice = 1
    for move in range(1, 4):
        if coins_left - move >= 0:
            score = minimax(coins_left - move, False)
            if score > best_score:
                best_score = score
                move_choice = move
    return move_choice

# ----- Game logic -----
def update_display():
    label.config(text=f"Coins remaining: {coins}")
    draw_coins()

def draw_coins():
    coin_canvas.delete("all")
    coin_color = "gold"
    radius = 20
    spacing = 10
    canvas_width = int(coin_canvas['width'])
    coins_per_row = max(1, (canvas_width - spacing) // (2 * radius + spacing))

    for i in range(coins):
        row = i // coins_per_row
        col = i % coins_per_row
        x = spacing + col * (2 * radius + spacing)
        y = spacing + row * (2 * radius + spacing)
        coin_canvas.create_oval(
            x, y, x + 2*radius, y + 2*radius,
            fill=coin_color, outline="darkorange", width=2
        )

def player_move(take):
    global coins
    if take > coins:
        return
    coins -= take
    update_display()

    if coins <= 0:
        end_game("🎉 You Win! 🎊")
        return

    info_label.config(text="🤖 AI is thinking...")
    root.after(800, ai_move)

def ai_move():
    global coins
    move = best_move(coins)
    coins -= move
    update_display()

    if coins <= 0:
        end_game("💻 AI Wins! Better luck next time.")
        return

    info_label.config(text=f"💻 AI took {move} coin{'s' if move > 1 else ''}. Your turn!")

def end_game(message):
    info_label.config(text="")
    result_label.config(text=message, fg="green" if "Win" in message else "red", font=("Arial", 16, "bold"))

    # Disable all buttons after game ends
    for child in button_frame.winfo_children():
        child.config(state="disabled")

# ----- UI setup -----
root = tk.Tk()
root.title("🪙 Nim Game - Player vs AI")
root.geometry("520x520")
root.resizable(True, True)

label = tk.Label(root, text=f"Coins remaining: {coins}", font=("Arial", 16))
label.pack(pady=10)

coin_canvas = tk.Canvas(root, width=480, height=200, bg="white",
                        highlightthickness=1, relief="ridge")
coin_canvas.pack(pady=10)

info_label = tk.Label(root, text="Your turn! Take 1, 2, or 3 coins.", font=("Arial", 12))
info_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

for i in range(1, 4):
    tk.Button(button_frame, text=f"Take {i}", font=("Arial", 14), width=8,
              command=lambda x=i: player_move(x)).grid(row=0, column=i, padx=10)

# Label for final result
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=10)

update_display()
root.mainloop()
