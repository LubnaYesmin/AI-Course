import heapq   # smallest heuristic value.

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    priority_queue = [(heuristics[start], start)]     # The smallest heuristic value will be processed first.
    came_from = {start: None}                        # Dictionary to track the parent node for path reconstruction.

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]             #  [::-1] reverses the path to display it from start to goal.

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                came_from[neighbor] = current
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))

    return None

# -----------------------------
# 🔹 Taking user input
# -----------------------------
graph = {}
heuristics = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

print("\nEnter heuristic values:")
for node in graph:
    h = int(input(f"Heuristic value for {node}: "))
    heuristics[node] = h

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# -----------------------------
# 🔹 Run Best-First Search
# -----------------------------
path = best_first_search(graph, heuristics, start, goal)

# -----------------------------
# 🔹 Output
# -----------------------------
print("\nResult:")
if path:
    print("Best-First Path:", " -> ".join(path))
else:
    print("No path found.")

