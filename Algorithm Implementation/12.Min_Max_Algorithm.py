def minimax(depth, node_index, is_maximizing, scores, max_depth):
    if depth == max_depth:
        return scores[node_index]

    if is_maximizing:
        best = float('-inf')
        for i in range(2):  # Two children: left (0) and right (1)
            val = minimax(depth + 1, node_index * 2 + i, False, scores, max_depth)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, scores, max_depth)
            best = min(best, val)
        return best

# -----------------------------------
# 🔹 User Input
# -----------------------------------
depth = int(input("Enter depth of game tree: "))  # Number of levels

leaf_nodes = 2 ** depth
print(f"\nEnter {leaf_nodes} leaf node scores (space-separated):")
scores = list(map(int, input().split()))

# -----------------------------------
# 🔹 Run Minimax
# -----------------------------------
optimal_value = minimax(0, 0, True, scores, depth)

# -----------------------------------
# 🔹 Output
# -----------------------------------
print("\nOptimal value (for maximizer):", optimal_value)
