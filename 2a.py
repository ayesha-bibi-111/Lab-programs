from collections import deque

# Defining the tree as an adjacency list
# Key = Parent Node, Value = List of Children
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def bfs(start_node):
    # Initialize a queue with the root node
    queue = deque([start_node])
    visited_order = []
    
    while queue:
        # Remove the node from the front of the queue
        current = queue.popleft()
        visited_order.append(current)
        
        # Add all children of the current node to the back of the queue
        for child in tree.get(current, []):
            queue.append(child)
            
    return visited_order

# --- Execution ---
result = bfs(1)

print("For BFS:", " ".join(map(str, result)))