#  Breadth-First Search (BFS)

## How BFS Works
The *Breadth-First Search (BFS)* algorithm explores a graph level by level, starting from a source node and visiting all its neighbors before moving to the next level.Uses a queue(FIFO-First In,First Out) data structure.

### Step-by-Step Process:
1. Start with a source node and mark it as *visited*.
2. Put the source node into a *queue*.
3. While the queue is not empty:
   - Dequeue a node.
   - Visit all *unvisited neighbors* of that node.
   - Enqueue all those neighbors.
4. Repeat until the queue is empty.

## Applications:
- Finding the shortest path in unweighted graphs.
- Web crawlers (exploring links level by level).
- Network broadcasting.
- Social network friend suggestions(Find connection path between users).

## Complexities
 
 - Time Complexity: O(b^d)
 - Space Complexity: O(b^d)
   where
   b = branching factor, d = depth of the shallowest goal node.

# Input/Output Screenshot
![ Input_Output_Screenshot](https://github.com/Shajeda708/AI-/blob/main/Algorithm_Implementation/BFS/Screenshot.png)


