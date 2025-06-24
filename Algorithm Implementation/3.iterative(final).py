def depth_limited_dfs_iterative(graph, start, limit):
    stack = [(start, 0)]
    visited = set()

    while stack:
        node, depth = stack.pop()
        if node not in visited and depth <= limit:
            print(node, end=" ")
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                stack.append((neighbor, depth + 1))

def iterative_deepening_search(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth Limit {depth}: ", end="")
        depth_limited_dfs_iterative(graph, start, depth)


graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter start node for IDS: ")
max_depth = int(input("Enter max depth limit: "))

# ------------------------------
# 🔹 Call IDS
# ------------------------------
print("\nIterative Deepening Search Traversal (Non-Recursive):")
iterative_deepening_search(graph, start_node, max_depth)
