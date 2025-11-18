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

def alphabeta(node, is_max, alpha, beta):
    if node in utilities:
        return min(utilities[node]), [node]

    children = tree[node]
    val, path = alphabeta(children[0], not is_max, alpha, beta)
    best_val = val
    best_path = [node] + path

    for child in children[1:]:
        val, path = alphabeta(child, not is_max, alpha, beta)
        if (is_max and val > best_val) or (not is_max and val < best_val):
            best_val = val
            best_path = [node] + path

        if is_max:
            alpha = max(alpha, best_val)
        else:
            beta = min(beta, best_val)

        if beta <= alpha:
            break

    return best_val, best_path

best_value, best_path = alphabeta(root, True, float('-inf'), float('inf'))
print("\nBest value for root (MAX):", best_value)
print("Best path:", " -> ".join(best_path))

