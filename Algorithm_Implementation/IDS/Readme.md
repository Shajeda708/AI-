# Iterative Deepening Search (IDS)

## Overview

Iterative Deepening Search (IDS) is a search algorithm that combines the space efficiency of Depth-First Search (DFS) with the completeness of Breadth-First Search (BFS).  

It works by repeatedly running Depth-Limited Search (DLS) with increasing depth limits until the goal is found.
In other words, it performs DFS multiple times — each time going one level deeper.



## How the Algorithm Works

### Step-by-Step Explanation:
1. Start with depth limit = 0.
2. Perform **Depth-Limited Search (DLS)** up to that depth.
3. If the goal is not found:
   - Increase the depth limit by 1.
   - Repeat the DLS.
4. Continue until:
   - The goal node is found, or
   - All nodes are visited.

## Applications:
- Used in *Artificial Intelligence* search problems where the search space is large but the solution depth is unknown.
- Commonly used in:
  - Route-finding
  - Puzzle solving (like the 8-puzzle)
  - Game tree search
  - Robot motion planning

## Complexity Analysis

Time Complexity : O(b^d) 
Space Complexity: O(b*d) 
Where: b = branching factor, d = depth of the solution 

- IDS uses less memory than BFS (like DFS),  
- Guarantees optimal solution (like BFS),  
- Slightly slower because it repeats searches at shallower depths.

# Input/Output Screenshot
![ Input_Output_Screenshot](https://github.com/Shajeda708/AI-/blob/main/Algorithm_Implementation/IDS/Screenshot1.png)
![ Input_Output_Screenshot](screenshot2.png)

