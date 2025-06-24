def depth_limited_dfs_iterative(graph, start, limit):
    stack = [(start, 0)]
    visited = set()
    
    # start is the node to begin from
    # 0 is the current depth (root level)

    while stack:                                              # Pop the last element from the stack. This gives you:  node: the current node to process
        node, depth = stack.pop()                             # depth: how deep you are from the start node
        if node not in visited and depth <= limit:            # Only process the node if: It hasn’t been visited Current depth is within the allowed limit
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
