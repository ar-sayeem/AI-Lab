def dfs_total_cost(graph):
    total_cost = sum(sum(edges.values()) for edges in graph.values())
    return total_cost


def dfs(graph, start):
    stack = [(0, start, [start])]  # (cost, node, path)
    paths = []

    while stack:
        cost, current, path = stack.pop()

        if not graph[current]:  # If leaf node
            paths.append((cost, path))

        for neighbor, edge_cost in graph[current].items():
            stack.append((cost + edge_cost, neighbor, path + [neighbor]))

    # print("All paths to leaf nodes:")
    # for cost, path in paths:
    #     print("Path:", path, "Cost:", cost)

    # Find and print the shortest path
    if paths:
        min_cost, min_path = min(paths)  # Automatically sorts by cost
        print("\nMinimum cost path:", min_path, "with cost:", min_cost)
    else:
        print("No valid path found.")


graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 1, 'E': 2},
    'C': {'F': 3, 'G': 4},
    'D': {'H': 2, 'I': 1},
    'E': {'J': 4, 'K': 3},
    'F': {'L': 2, 'M': 3},
    'G': {'N': 1, 'O': 1},
    'H': {},
    'I': {},
    'J': {},    
    'K': {},
    'L': {},
    'M': {},
    'N': {},
    'O': {}
}

total_cost = dfs_total_cost(graph)
print("Total cost of the tree:", total_cost)
dfs(graph, 'A')
