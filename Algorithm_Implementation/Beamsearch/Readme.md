# Beam Search

## How the Algorithm Works
Beam Search is a *heuristic search algorithm* similar to Best-First Search but keeps only a *fixed number of best nodes (beam width)* at each level.  
- Reduces memory usage compared to Best-First.  
- Does *not guarantee optimal solution*.

## Steps
- Start with the initial node.
- Generate all successors of the current node.
- Evaluate each successor using a heuristic function h(n) (how close it seems to the goal).
- Sort successors by heuristic value (best first).
- Keep only the top k nodes — this is your beam width.
- Expand those k nodes in the next iteration.
- Repeat until:
   Goal is found, or
   No nodes left to expand.

## Applications:
1. Natural Language Processing(machine traslation,sentence geberation)
2. Speech Recognition(word sequence prediction)
3. Game AI(predicting best moves efficiently)
4. Robot path planning(for large state spaces)

## Complexities
- Time : O(b*d) for small beam width k << b 
- Space:  O(k*d) 

# Input/Output Screenshot

![ Input_Output_Screenshot](https://github.com/Shajeda708/AI-/blob/main/Algorithm_Implementation/Beamsearch/Screenshot.png)
