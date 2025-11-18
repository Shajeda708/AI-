# Depth-Limited Search (DLS)

## Overview

*Depth-Limited Search (DLS)* is a variation of *Depth-First Search (DFS)* where the depth of the search is *restricted* to a specific limit.  
It helps prevent infinite loops in deep or cyclic graphs by stopping the search once the specified *depth limit* is reached.

It is especially useful when we know that the *goal node is not far* from the starting node.

## How the Algorithm Works

### Step-by-Step Explanation:
1. Start from the source node.
2. Keep track of the current depth.
3. If the current depth > limit, stop exploring that path (return).
4. Visit the node and mark it as visited.
5. For each unvisited neighbor, recursively perform Depth-Limited Search with the depth incremented by 
6. Continue until:
   - The goal node is found, or
   - The depth limit is reached.

## Applications:
- To avoid infinite loops
- Robot path planning
- Used in AI search Problems forms the basis of Iterative Deepening Search
- In game tree search used to explore limited moves in a game

## Complexity Analysis

- Time Complexity:   O(b^l) 
- Space Complexity:  O(b*l) 
Where:  b = branching factor, l = depth limit 
DLS can miss the goal if it lies beyond the depth limit, but it saves both time and space.

# Input/Output Screenshot
![ Input_Output_Screenshot](https://github.com/Shajeda708/AI-/blob/main/Algorithm_Implementation/DLS/Screenshot1.png)
![ Input_Output_Screenshot](https://github.com/Shajeda708/AI-/blob/main/Algorithm_Implementation/DLS/Screenshot2.png)






