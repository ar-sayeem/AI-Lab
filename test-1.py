def dfs_total_cost(graph):
    total_cost = 0
    for node in graph:
        total_cost += sum(graph[node].values())
    return total_cost


def dfs(graph, start):
    stack = [(0, start, [start])]
    paths = []

    while stack:
        cost, current, path = stack.pop()

        if not graph[current]:
            paths.append((cost, path))

        for neighbor, edge_cost in graph[current].items():
            stack.append((cost + edge_cost, neighbor, path + [neighbor]))

    if paths:
        min_cost, min_path = min(paths)
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
