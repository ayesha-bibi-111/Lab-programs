# Defining the tree as an adjacency list
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def dfs(node, visited_order=None):
    if visited_order is None:
        visited_order = []
    
    # Add the current node to our path
    visited_order.append(node)
    
    # Explore each child recursively (Depth-First)
    for child in tree.get(node, []):
        dfs(child, visited_order)
        
    return visited_order

# --- Execution ---
result = dfs(1)

# Format the output to match your requirement
print("For DFS:", " ".join(map(str, result)))