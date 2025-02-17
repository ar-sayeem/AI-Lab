Graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 1, 'E': 3},
    'C': {'F': 3, 'G': 2},
    'D': {'H': 3, 'I': 1},
    'E': {'J': 3, 'K': 5},
    'F': {'L': 2, 'M': 4},
    'G': {'N': 4, 'O': 3},
    'H': {}, 'I': {}, 'J': {}, 'K': {}, 'L': {}, 'M': {}, 'N': {}, 'O': {}
}

def dfs_shortest_leaf(graph, start):
    stack = [(start, 0, [start])]
    shortest_path, min_cost = None, float('inf')
    
    while stack:
        node, cost, path = stack.pop()
        if not graph[node]:
            if cost < min_cost:
                min_cost, shortest_path = cost, path
        else:
            for neighbor, weight in graph[node].items():
                stack.append((neighbor, cost + weight, path + [neighbor]))
    
    return shortest_path, min_cost

path, cost = dfs_shortest_leaf(Graph, 'A')
print("Shortest DFS Path:", " -> ".join(path))
print("Total Cost:", cost)
