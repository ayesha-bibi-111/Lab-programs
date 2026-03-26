def dls(tree, node, depth, visited):
    # Visit current node
    visited.append(node)

    # If depth limit reached, stop
    if depth == 0:
        return

    # Recur for children
    for child in tree.get(node, []):
        dls(tree, child, depth - 1, visited)


def iddfs(tree, start, max_depth):
    for depth in range(max_depth + 1):
        visited = []
        dls(tree, start, depth, visited)

        print(f"Depth Limit {depth}: Visited nodes {visited}")


# Tree representation
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# Run IDDFS
iddfs(tree, start=1, max_depth=2)