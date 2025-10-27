graph = {}

n = int(input("Enter number of edges: "))


for _ in range(n):
    u, v = input("Enter edge (u v): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)  

start = input("Enter starting node: ")


visited =[]
queue = [start]

while queue:
    node = queue.pop(0)
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        queue.extend(graph[node])
