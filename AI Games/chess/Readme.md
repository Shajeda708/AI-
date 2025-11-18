## Human vs AI Chess Game (Python Tkinter)

## Description

This project is a simple Chess game with AI developed in Python using the tkinter GUI library and the python-chess package for chess logic.
The AI opponent uses the Minimax algorithm with Alpha-Beta pruning, evaluating possible board states up to a fixed depth to make optimal moves.

The player plays as White, and the AI plays as Black.

## How to Run the Game

# Steps:

1. Install Python
Make sure to have Python 3.8+ installed on your system.
Check by running:

python --version

2. Install Required Libraries
Open your terminal or command prompt and install dependencies:

pip install python-chess

(Tkinter is built-in with Python; no separate installation needed on most systems.)

3. Run the Game Save the source code in a file named, for example, chess_game.py, then run:

python chess_game.py

4. The game window will open, and you can start playing!

# Pre-Requisites
Python 3.8+	- Required to run the game
python-chess - Provides board representation, legal move generation, and chess rules
tkinter -   used for GUI rendering of the chessboard and pieces

Install dependencies via:

pip install python-chess

# How to Play

- You play as White, and the AI plays as Black.
- Click on a white piece to select it.
- The highlighted blue squares show legal moves for that piece.
- Click on a destination square to move.
- When a pawn reaches the last rank, a prompt allows you to choose promotion (Queen, Rook, Bishop, or      Knight).
- The AI will automatically make its move after yours.
- The game ends when:
    - Checkmate
    - Stalemate
    - Draw (insufficient material or repetition)

# Game Screenshots
![Chees_Game Screenshot](https://github.com/Shajeda708/AI-/blob/main/AI%20Games/chess/Images/Screenshot1.png)
![Chees_Game Screenshot](https://github.com/Shajeda708/AI-/blob/main/AI%20Games/chess/Images/Screenshot2.png)
![Chees_Game Screenshot](https://github.com/Shajeda708/AI-/blob/main/AI%20Games/chess/Images/Screenshot3.png)





