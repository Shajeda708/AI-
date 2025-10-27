graph = {}
n = int(input("Enter number of edges: "))


for _ in range(n):
    u, v, w = input("Enter edge (u v cost): ").split()
    w = int(w)
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))  


heuristic = {}
for node in graph:
    heuristic[node] = int(input(f"Heuristic[{node}]: "))

start = input("Enter start: ")
goal = input("Enter goal: ")

visited =set()
queue = [(heuristic[start], 0, start, [start])]

while queue:
    
    queue.sort(key=lambda x: x[0])
    f, g, node, path = queue.pop(0)

    if node in visited:
        continue
    visited.add(node)

    print(node, end=" ")

    if node == goal:
        print("\nGoal reached!")
        print("Path:", " -> ".join(path))
        print("Total cost:", g)
        print("values:",heuristic[2])
        break

    for neighbor, cost in graph[node]:
        if neighbor not in visited:
            g_new = g + cost
            f_new = g_new + heuristic[neighbor]
            queue.append((f_new, g_new, neighbor, path + [neighbor]))

