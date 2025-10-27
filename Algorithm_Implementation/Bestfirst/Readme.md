# Best-First Search (BFS)

## How the Algorithm Works

Best-First Search is a graph search algorithm that explores a graph by always expanding the most promising node based on a heuristic function (h(n)) — an estimate of how close each node is to the goal.

Unlike BFS (Breadth-First Search), which explores all nodes level by level, Best-First Search uses a priority queue to explore nodes that appear closer to the goal first.



###  Steps of the Algorithm

- Start with the initial node, add it to the open list.
- Select the node with the lowest heuristic value (h).
- If the node is the goal, stop and return the path.
- Otherwise, expand its neighbors and add them to the open list.
- Repeat until the goal is found or no nodes remain.

## Applications:
- Pathfinding and navigation (in games, maps, and robotics)
- Speech and Image Recognization
- AI in games (for NPCs moving toward a target)
- Network routing (chooses paths based on least cost or lowest latency)
- Solving puzzles (8-puzzle, maze navigation)

## Complexities

- Time Complexity:   O(b^d) 
- Space Complexity:  O(b^d) 

# Input/Output Screenshot
![ Input_Output_Screenshot](https://github.com/Shajeda708/AI-/blob/main/Algorithm_Implementation/Bestfirst/Screenshot.png)


