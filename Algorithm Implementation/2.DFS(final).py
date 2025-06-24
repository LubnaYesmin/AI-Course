def dfs_stack(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors in reverse to maintain order (optional)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
                    
# -----------------------------
# 🔹 Build the Graph
# -----------------------------
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter start node for DFS: ")

# -----------------------------
# 🔹 Run DFS (Using Stack)
# -----------------------------
print("\nDFS Traversal (using stack):")
dfs_stack(graph, start_node)