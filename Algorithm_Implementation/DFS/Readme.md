# Depth-First Search (DFS)

##  How DFS works

*Depth-First Search (DFS)* is a *graph traversal algorithm* that explores as far as possible along a branch before *backtracking*.  
It starts from a source node and explores *each branch completely* before moving to another branch.

DFS can be implemented *recursively* or *using a stack*.

# Step-by-step process:

1. Start from any node (usually called the source).
2. Mark the starting node as visited.
3. Explore one of its unvisited neighbors.
4. Repeat the process (go deeper) until there are no more unvisited neighbors.
5. Backtrack to the previous node and continue exploring other unvisited neighbors.
6. Continue until all nodes are visited.

# Applications of DFS:

- Pathfinding in mazes and puzzles
- Topological sorting
- Detecting cycles in graphs
- Finding connected components in a network
- Solving recursive problems (e.g., Sudoku)

# Complexities:
- Time Complexity:O(b^m)
- Space complexity:O(b*m)

# Input/Output Screenshot
![ Input_Output_Screenshot](screenshot.png)
