def dfs_stack(graph, start_node):
    visited = set()
    stack = [start_node]  # A list named stack is initialized with the start_node inside it.
                          # This will be used to manage the DFS traversal using LIFO (Last In, First Out) order.


    while stack:          # This while loop will continue running as long as there is at least one node in the stack.
        node = stack.pop()
        if node not in visited:    # Checks if this node has already been visited.
                                   # If not, we’ll now process and mark it as visited.
            print(node, end=" ")
            visited.add(node)
            # Add neighbors in reverse to maintain order (optional)
            for neighbor in reversed(graph.get(node, [])):        # reversed(...) is used so that neighbors are pushed onto the stack in reverse order — this helps maintain the original input order when popping.
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







# non visited ----- stack 
# visited --------- node 

