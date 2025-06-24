import heapq

def a_star_search(graph, heuristics, start, goal):
    open_set = [(heuristics[start], 0, start)]  # (f = g + h, g, node)
    came_from = {start: None}
    g_cost = {start: 0}
    visited = set()

    while open_set:
        f, g, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor in visited:
                continue

            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + heuristics.get(neighbor, 0)
                came_from[neighbor] = current
                heapq.heappush(open_set, (f, new_g, neighbor))

    return None

# -----------------------------
# 🔹 Taking User Input
# -----------------------------
graph = {}
heuristics = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node name: ")
    neighbors_input = input(f"Enter neighbors of {node} with cost (e.g., B:2 C:3): ").split()
    neighbors = []
    for item in neighbors_input:
        neighbor, cost = item.split(":")
        neighbors.append((neighbor, int(cost)))
    graph[node] = neighbors

print("\nEnter heuristic values:")
for node in graph:
    h = int(input(f"Heuristic for {node}: "))
    heuristics[node] = h

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# -----------------------------
# 🔹 Run A* Search
# -----------------------------
path = a_star_search(graph, heuristics, start, goal)

# -----------------------------
# 🔹 Output
# -----------------------------
print("\nResult:")
if path:
    print("A* Path:", " -> ".join(path))
else:
    print("No path found.")

