## Minimax Algorithm

## How minimax works

Minimax is a decision-making algorithm used mostly in two-player games (like Tic-Tac-Toe, Chess, Checkers, etc.) where one player tries to maximize their score and the other tries to minimize it.

It works by simulating all possible moves, assuming that both players play optimally —
- One player is the MAX (tries to get the highest score)
- The other is the MIN (tries to minimize MAX’s score)
At each level of the game tree:
- The Maximizer chooses the move with the maximum value.
- The Minimizer chooses the move with the minimum value.

## Step-by-Step Working
1. Construct a game tree of all possible moves up to a certain depth.
2. Assign utility values (scores) to terminal nodes:
Positive values → Favorable to MAX
Negative values → Favorable to MIN
3. Propagate the scores upward:
MAX nodes choose the maximum value of their children.
MIN nodes choose the minimum value of their children.
4. The value at the root node represents the best guaranteed outcome for MAX, assuming both players play optimally.
5. Choose the move that leads to this optimal value.

## Application
- used in two player games(Tic-Tac-Toe,Chees,Connect Four)
- Decision-Making Systems(financial or risk-based simulations)
- Adversarial Planning(Plan for worst-case scenarios)
- AI palnning(Multi-agent robotics)


## Complexity
- Time complexity: O(b^d)
- Space complexity:O(b*d)
Where - b =branching factor,d=depth of the game tree

# Input/Output Screenshot
![ Input_Output_Screenshot](screenshot.png)