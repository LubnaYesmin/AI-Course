def depth_limited_search(graph, current, goal, limit, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    path.append(current)
    visited.add(current)

    if current == goal:
        return path

    if limit <= 0:
        path.pop()
        return None

    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            result = depth_limited_search(graph, neighbor, goal, limit - 1, visited, path) # go to the neighbor node, decreasing the limit by 1.
            if result:                                                                     # backtracking 
                return result

    path.pop()                 # if no node is found , backtarck
    return None

# -----------------------------
# 🔹 Taking user input
# -----------------------------
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")
depth_limit = int(input("Enter depth limit: "))

# -----------------------------
# 🔹 Run Depth-Limited Search
# -----------------------------
result = depth_limited_search(graph, start_node, goal_node, depth_limit)

print("\nResult:")
if result:
    print("Path found:", " -> ".join(result))
else:
    print("No path found within the depth limit.")
