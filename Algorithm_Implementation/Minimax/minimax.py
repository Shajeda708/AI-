tree = {}
utilities = {}

n = int(input("Enter number of internal nodes with children: "))
for _ in range(n):
    data = input().split()
    tree[data[0]] = data[1:]

m = int(input("Enter number of leaf nodes with utilities: "))
for _ in range(m):
    data = input().split()
    utilities[data[0]] = list(map(int, data[1:]))

root = input("Enter root node (MAX): ")

def minimax(node, is_max):
    if node in utilities:
        return (max(utilities[node]) if is_max else min(utilities[node])), [node]

    children = tree[node]
    val, path = minimax(children[0], not is_max)
    best_val = val
    best_path = [node] + path

    for child in children[1:]:
        val, path = minimax(child, not is_max)
        if (is_max and val > best_val) or (not is_max and val < best_val):
            best_val = val
            best_path = [node] + path

    return best_val, best_path

best_value, best_path = minimax(root, True)
print("\nBest value for root (MAX):", best_value)
print("Best path:", " -> ".join(best_path))

