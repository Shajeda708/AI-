##  Tic Tac Toe (Minimax AI)

# Description

This project is a simple Tic Tac Toe game with an AI opponent, created using Python and Tkinter.
The player competes against the computer, which uses the Minimax algorithm to always play optimally — making it impossible to beat if played correctly!

This version includes:
- A clean Graphical User Interface (GUI)
- Player vs AI mode
- A Reset button to restart the game easily

##  How to Run
# Steps:
1. Install Python
Ensure that Python 3.8 or higher is installed.
You can check with:

python --version

2. Run the Game
Save the source code in a file named tic_tac_toe_ai.py and run:

python tic_tac_toe_ai.py

The GUI window will open, and you can start playing immediately.

## Requirements / Libraries

No external libraries are required except Tkinter, which comes built-in with Python.

## How to Play

- You play as X, and the AI plays as O.
- Click on any empty square to make your move.
- The AI will immediately respond using the Minimax algorithm.
- The game ends when either:
    - You win 
    - The AI wins 
    - Or it’s a tie 
- You can click Reset to start a new round.

## Screenshots
![Game Screenshot](https://github.com/Shajeda708/AI-/blob/main/AI%20Games/Tictactoe/Images/Screenshot1.png)
![Game Screenshot](https://github.com/Shajeda708/AI-/blob/main/AI%20Games/Tictactoe/Images/Screenshot2%20.png)
![Game Screenshot](Images/screenshot3.png)


## Algorithm used (Minimax):
The Minimax algorithm is used in two-player turn-based games (like Tic Tac Toe, Chess, etc.).
Its goal is to make the best possible move by minimizing the possible loss in a worst-case scenario.

It assumes:
- The AI (O) plays optimally (tries to maximize its score).
- The Player (X) also plays optimally (tries to minimize the AI’s score).
## How it works on the game

## Player Turn

1. The game starts with an empty 3×3 board.
    - Each cell is a button on the Tkinter window.
2. When the player clicks on a cell:
    - The function player_move(i) runs.
    - It checks if that cell is empty.
    - If it’s empty, it places the player’s symbol “X” there.
3. The button’s text becomes “X” and is disabled (so it can’t be clicked again).
4. After the player’s move:
    - The program checks if the player has won using check_winner().
    - If the player wins → it shows “You Win!” on the screen.
    - If not → it becomes AI’s turn. Turn

## AI turn(Minimax)
1. AI’s turn starts →  calls ai_move().
2. The AI looks at the board and checks every empty box one by one.
3. For each empty box:
    - The AI pretends to play its move (“O”) there.
    - Then it uses the Minimax algorithm to imagine what will happen next:
        - What move will the player (“X”) make after this?
        - What move will AI make after that?
        - And so on… until the game ends (win, lose, or draw).
4. The Minimax function gives each possible move a score:
    - +1 → AI wins in the end
    - 0 → The game ends in a tie
    - -1 → The player wins in the end
5. The AI compares all the scores and picks the move with the highest score — the move that helps it win or at least draw.
6. The AI then plays that move on the board.




