from collections import deque

# Function to perform BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph.get(node, []):
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