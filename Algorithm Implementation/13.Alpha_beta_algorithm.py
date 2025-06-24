def alpha_beta(depth, node_index, is_max, scores, alpha, beta, max_depth):
    if depth == max_depth:  # Leaf node
        return scores[node_index]

    if is_max:
        max_eval = float('-inf')
        for i in range(2):  # left and right
            eval = alpha_beta(depth + 1, node_index * 2 + i, False, scores, alpha, beta, max_depth)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)      # Update alpha if we find a better value.

            if beta <= alpha:
                break  
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            eval = alpha_beta(depth + 1, node_index * 2 + i, True, scores, alpha, beta, max_depth)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            if beta <= alpha:
                break       # beta <= alpha, we cut off the branch.
        return min_eval
    
    # -----------------------------
# 🔹 User Input
# -----------------------------
depth = int(input("Enter depth of game tree: "))
leaf_nodes = 2 ** depth

print(f"\nEnter {leaf_nodes} leaf node values (space-separated):")
scores = list(map(int, input().split()))

# -----------------------------
# 🔹 Run Alpha-Beta Pruning
# -----------------------------
alpha = float('-inf')
beta = float('inf')

optimal_value = alpha_beta(0, 0, True, scores, alpha, beta, depth)

# -----------------------------
# 🔹 Output
# -----------------------------
print("\nOptimal value (with Alpha-Beta pruning):", optimal_value)

