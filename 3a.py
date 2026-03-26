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

def dls(node, limit, current_depth, visited):
    """Depth-Limited Search logic"""
    if current_depth <= limit:
        visited.append(node)
        for neighbor in tree.get(node, []):
            dls(neighbor, limit, current_depth + 1, visited)
    return visited

def iddfs(root, max_depth):
    """Iterative Deepening logic"""
    print("--- IDDFS Progression ---")
    for limit in range(max_depth + 1):
        visited = []
        result = dls(root, limit, 0, visited)
        print(f"Depth Limit {limit}: Visited nodes {result}")

# --- Execution ---

# 1. Standard DLS at Depth 2
print("--- DLS (Limit 2) ---")
print(f"Visited nodes: {dls(1, 2, 0, [])}\n")

# 2. IDDFS up to Depth 2
iddfs(1, 2)