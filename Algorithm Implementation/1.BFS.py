from collections import deque        # This imports deque from Python's collections module

# Function to perform BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])         # Initializes a deque called queue and adds the start node to it.

    while queue:
        node = queue.popleft()     # Removes (pops) the leftmost node from the queue and stores it in node.
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph.get(node, []):     # Loops through all neighbors of the current node.

                                                     # graph.get(node, []) returns the list of neighbors of node.

                                                     # If node doesn’t exist in the graph (edge case), it returns an empty list.
                if neighbor not in visited:
                    queue.append(neighbor)


# Taking user input for graph
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter start node for BFS: ")

# Call BFS
print("\nBFS Traversal:")
bfs(graph, start_node)
