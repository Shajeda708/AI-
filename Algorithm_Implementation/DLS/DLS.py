graph = {}
n = int(input("Enter number of edges: "))


for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)  

start = input("Enter start node: ")
target = input("Enter target node: ")
limit = int(input("Enter depth limit: "))

stack = [(start, 0)] 
visited = []

while stack:
    node, depth = stack.pop()
    if node not in visited and depth <= limit:
        visited.append(node)
        if node == target:
            print("Target found!")
            print("Path:", " -> ".join(visited))
            break
        for neighbor in reversed(graph.get(node, [])):
            stack.append((neighbor, depth + 1))
else:
    print("Target not found within depth limit")

