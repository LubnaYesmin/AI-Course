def hill_climbing(graph, heuristics, start):
    current = start # Set current node to the start node.
    path = [current]

    while True:
        neighbors = graph.get(current, []) # Get all the neighbors of the current node from the graph.  f the node has no neighbors, it returns an empty list.
        if not neighbors:
            break

        next_node = None
        min_h = heuristics[current]

        for neighbor in neighbors:
            if heuristics[neighbor] < min_h:  # Minimization
                min_h = heuristics[neighbor]
                next_node = neighbor

        if next_node is None:
            break  # No better neighbor

        current = next_node  # Move to the next_node.
        path.append(current)

    return path


# -----------------------------
# 🔹 User Input
# -----------------------------
graph = {}
heuristics = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

print("\nEnter heuristic values (lower is better):")
for node in graph:
    h = int(input(f"Heuristic for {node}: "))
    heuristics[node] = h

extra = int(input("Enter number of leaf nodes (not in main graph): "))
for _ in range(extra):
    node = input("Leaf node name: ")
    h = int(input(f"Heuristic for {node}: "))
    heuristics[node] = h

start_node = input("\nEnter start node: ")

# -----------------------------
# 🔹 Run Hill Climbing
# -----------------------------
path = hill_climbing(graph, heuristics, start_node)

# -----------------------------
# 🔹 Output
# -----------------------------
print("\nPath found by Hill Climbing:")
print(" -> ".join(path))
print(f"Final heuristic value: {heuristics[path[-1]]}")
