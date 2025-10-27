# Bidirectional Search

## How the Algorithm Works
Bidirectional Search is an informed search algorithm used to find the shortest path between a source (start node) and a goal node in a graph.

Instead of searching from the start node to the goal like BFS or DFS, it runs two simultaneous searches:
- One forward from the start node
- One backward from the goal node

These two searches continue until they meet in the middle — drastically reducing the search space and improving efficiency.

### Step-by-Step Process:
1. Initialize two queues: **forward** and **backward**.
2. Perform BFS from both sides alternately.
3. After each step, check if any node has been visited by both searches.
4. If yes → A path is found.
5. Combine the two partial paths (from start to meeting point and from goal to meeting point).
6. Stop the algorithm.

## Applications:
- Finding the shortest route in maps and navigation systems (Google Maps, GPS).
- Social network analysis (finding the shortest connection between two users).
- Robot motion planning.
- AI game development (like pathfinding in chess or puzzles).

## Complexity
- Time Complexity: O(b^(d/2))  
  (Much faster than BFS O(b^d))
- Space Complexity: O(b^(d/2))
 
# Input/Output Screenshot
![ Input_Output_Screenshot](screenshot.png)

