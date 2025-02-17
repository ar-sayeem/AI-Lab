def dfs(Graph, start):
    stack = [(0, start, [start])]  # (cost, node, path)
    paths = []

    while stack:
        cost, current, path = stack.pop()

        if len(path) == 4:    // based on question tree
            paths.append((cost,current, path))

        for neighbor, edge_cost in Graph[current].items():
            stack.append((cost + edge_cost, neighbor, path + [neighbor]))

    # Display all paths of length 4
    print("All paths of length 4:")
    for path in paths:
        print(path)

    # Find and print the shortest path
    if paths:
        shortest_path = min(paths)  # Automatically sorts by cost
        print("\nShortest path:", shortest_path)
    else:
        print("No valid path of length 4 found.")

# Example Graph
Graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 1, 'E': 3},
    'C': {'F': 3, 'G': 2},
    'D': {'H': 3, 'I': 1},
    'E': {'J': 3, 'K': 5},
    'F': {'L': 2, 'M': 4},
    'G': {'N': 4, 'O': 3},
    'H': {},
    'I': {},
    'J': {},
    'K': {},
    'L': {},
    'M': {},
    'N': {},
    'O': {}
}

dfs(Graph, 'A')
