graph = {}
n = int(input("Enter number of edges: "))

for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

heuristic = {}
for node in graph:
    heuristic[node] = int(input(f"Heuristic[{node}]: "))

start = input("Enter start: ")
goal = input("Enter goal: ")
beam_width = int(input("Enter beam width: "))

visited = []
queue = [(start, [start])]

while queue:
    # Sort by heuristic and keep only top 'beam_width' nodes
    queue = sorted(queue, key=lambda x: heuristic[x[0]])[:beam_width]
    node, path = queue.pop(0)

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        if node == goal:
            print("\nGoal reached!")
            print("Path:", " -> ".join(path))
            print("Heuristic values along path:", [heuristic[n] for n in path])
            break

        for nei in graph[node]:
            if nei not in visited:
                queue.append((nei, path + [nei]))
else:
    print("\nPath not found!")
