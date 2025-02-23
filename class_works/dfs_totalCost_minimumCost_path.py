def dfs_total_cost(graph):
    total_cost = 0
    for node in graph:
        total_cost += sum(graph[node].values())
    return total_cost


def dfs_min_cost_path(graph, start):
    stack = [(start, [start], 0)]  # (current_node, path, cost)
    min_cost = float('inf')
    min_path = []
    
    while stack:
        node, path, cost = stack.pop()
        
        if not graph[node]:  # If leaf node
            if cost < min_cost:
                min_cost = cost
                min_path = path
        
        for neighbor, edge_cost in graph[node].items():
            stack.append((neighbor, path + [neighbor], cost + edge_cost))
    
    return min_cost, min_path


# Given tree graph
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
min_cost, min_path = dfs_min_cost_path(graph, 'A')

print("Total cost of the tree:", total_cost)
print("Minimum cost path:", min_path, "with cost:", min_cost)
