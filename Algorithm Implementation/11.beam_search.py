import heapq

def beam_search(graph, heuristics, start, goal, beam_width):
    queue = [(heuristics[start], [start])]
    
    while queue:
        # Sort by heuristic and trim to beam width
        queue = sorted(queue, key=lambda x: heuristics[x[1][-1]])[:beam_width] # Sort the queue based on the heuristic value of the last node in each path.Only keep the top beam_width paths (best ones).
                                                                                # heuristics[x[1][-1]] → heuristic value of that last node.
        new_queue = []
        
        for _, path in queue:
            current = path[-1]            # Set current as the last node of the path.
            
            if current == goal:
                return path
            
            for neighbor in graph.get(current, []):  # If there are no neighbors, [] is returned (safe).
                if neighbor not in path:  # avoid cycles
                    new_path = list(path)
                    new_path.append(neighbor)
                    new_queue.append((heuristics[neighbor], new_path))
        
        queue = new_queue

    return None

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

print("\nEnter heuristic values:")
for node in graph:
    h = int(input(f"Heuristic for {node}: "))
    heuristics[node] = h

extra = int(input("Enter number of leaf nodes (not already in graph): "))
for _ in range(extra):
    node = input("Leaf node name: ")
    h = int(input(f"Heuristic for {node}: "))
    heuristics[node] = h

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")
beam_width = int(input("Enter beam width: "))

# -----------------------------
# 🔹 Run Beam Search
# -----------------------------
path = beam_search(graph, heuristics, start, goal, beam_width)

# -----------------------------
# 🔹 Output
# -----------------------------
print("\nBeam Search Result:")
if path:
    print(" -> ".join(path))
else:
    print("No path found.")

