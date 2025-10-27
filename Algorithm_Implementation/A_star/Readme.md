## A* Algorithm 

## HoW A* works

A* is an informed search algorithm that finds the shortest (optimal) path from a start node to a goal node using both:
- Actual cost so far (g(n))
- Estimated cost to goal (h(n))
uses the formula - f(n)=g(n)+h(n) 
Where:
- g(n) → Actual cost from the start node to current node n.
- h(n) → Estimated (heuristic) cost from node n to goal.
- f(n) → Total estimated cost of the path through n.
 The node with the lowest f(n) is expanded first.

## Step-by-step working
1. Initialize
    - Create an OPEN list (priority queue) to store nodes to be explored.
    - Create a CLOSED list to store nodes already explored.
    - Add the start node to the OPEN list with f(start) = g(start) + h(start).
2. Loop
    - Pick the node n from the OPEN list with the lowest f(n).
    - If n is the goal, stop — you’ve found the optimal path!
    - Move n to the CLOSED list.
    - For each neighbor of n:
        - Calculate g(neighbor) = g(n) + cost(n, neighbor)
        - Calculate h(neighbor) (heuristic)
        - Calculate f(neighbor) = g(neighbor) + h(neighbor)
        - If the neighbor is already in OPEN or CLOSED with a lower f, skip it.
        - Otherwise, add/update it in the OPEN list.
3. Repeat until:
    - Goal is found, or
    - OPEN list becomes empty (no path exists).

## Application:
- Pathfinding in games (e.g., Pac-Man, Google Maps)
- Robot navigation
- Route optimization
- AI Planning and Puzzle solving (like 8-puzzle)

## Complexity:
- Time complexity:O(b^d)
- Space complexity:O(b^d)
Where:
b= branching factor
d=depth of the solution

# Input/Output Screenshot
![ Input_Output_Screenshot](https://github.com/Shajeda708/AI-/blob/main/Algorithm_Implementation/A_star/Screenshot.png)

