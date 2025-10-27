graph = {}
n = int(input("Enter number of edges: "))


for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)  

start = input("Enter start node: ")
target = input("Enter target node: ")
max_limit = int(input("Enter maximum depth limit: "))

def dls(node, target, limit, path):
    if limit < 0:
        return False
    path.append(node)
    if node == target:
        return True
    for neighbor in graph.get(node, []):
        if neighbor not in path:
            if dls(neighbor, target, limit-1, path):
                return True
    path.pop()
    return False

for depth in range(max_limit + 1):
    path = []
    if dls(start, target, depth, path):
        print("Target found!")
        print("Path:", " -> ".join(path))
        break
else: 
    print("Target not found within maximum depth limit")

