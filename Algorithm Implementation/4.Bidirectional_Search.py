from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]         # If start and goal are the same ,path is just the start node

    # Queues for BFS from both sides
    queue_start = deque([start])       # deque is used for efficient queue operations
    queue_goal = deque([goal])

    # Visited dictionaries to track paths
    visited_from_start = {start: None}
    visited_from_goal = {goal: None}

    while queue_start and queue_goal:   # keep running as long as both queues have nodes to explore
        # Expand from start side
        current_start = queue_start.popleft()
        for neighbor in graph.get(current_start, []):
            if neighbor not in visited_from_start:
                visited_from_start[neighbor] = current_start   # Record its parent and add to the queue
                queue_start.append(neighbor)
                if neighbor in visited_from_goal:
                    return construct_path(neighbor, visited_from_start, visited_from_goal) # If the neighbor was already visited from the goal side, we’ve found the meeting point!

        # Expand from goal side
        current_goal = queue_goal.popleft()
        for neighbor in graph.get(current_goal, []):
            if neighbor not in visited_from_goal:
                visited_from_goal[neighbor] = current_goal
                queue_goal.append(neighbor)
                if neighbor in visited_from_start:
                    return construct_path(neighbor, visited_from_start, visited_from_goal)

    return None

def construct_path(meeting_point, visited_from_start, visited_from_goal):
    path = []          # to store final path from start to goal.

    # From meeting point to start
    node = meeting_point
    while node:
        path.append(node)
        node = visited_from_start[node]
    path.reverse()

    # From meeting point to goal
    node = visited_from_goal[meeting_point]
    while node:
        path.append(node)
        node = visited_from_goal[node]

    return path

graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

path = bidirectional_search(graph, start_node, goal_node)

print("\nResult:")
if path:
    print("Path found:", " -> ".join(path))
else:
    print("No path found.")

