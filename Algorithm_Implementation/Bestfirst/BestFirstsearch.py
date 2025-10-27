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

visited = []
queue = [(start, [start])]   

while queue:
    
    queue.sort(key=lambda x: heuristic[x[0]])
    node, path = queue.pop(0)

    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        if node == goal:
            print("\nGoal reached!")
            print("Path:", " -> ".join(path))
            break

        for nei in graph[node]:
            if nei not in visited:
                queue.append((nei, path + [nei]))

else:
    print("\nPath not found!")

