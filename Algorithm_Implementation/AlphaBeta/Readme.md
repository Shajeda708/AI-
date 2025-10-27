## AlphaBeta prunning Algorithm

## How the algorithm works
Alpha–Beta Pruning is an optimization of the Minimax algorithm used in two-player games to reduce the number of nodes evaluated in the search tree.

It “prunes” (cuts off) branches that cannot possibly affect the final decision.

The algorithm keeps track of two parameters:

- α (alpha): The best value that the MAX player can guarantee so far.
- β (beta): The best value that the MIN player can guarantee so far.

During tree traversal:

At MAX nodes:
Update α = max(α, currentValue)

At MIN nodes:
Update β = min(β, currentValue)

Pruning condition:
If at any point β ≤ α, the remaining branches will not be explored (because they cannot influence the outcome).

## Steps of Alpha–Beta Pruning Algorithm

- Start with the root node (initial state).
- Initialize α = -∞ and β = +∞.
- Apply Minimax recursively, but at each step:
- Update α when a Max node improves its best value.
- Update β when a Min node improves its best value.
- Prune the remaining child nodes if β ≤ α.
- Continue until the entire tree is evaluated or pruned.
- The root value gives the best possible move.

## Application
- Game AI(Faster and optimal move selection)
- Robotics(minimize time in adverssrial paths)
- Decision making(choose best counter action)
- Security AI(plan defense stratagies)

## Complexity
- Time complexity:O(b^(d/2))
- Space complexity:O(b*d)

# Input/Output Screenshot
![ Input_Output_Screenshot](screenshot.png)

- Space complexity:O(b*d)
