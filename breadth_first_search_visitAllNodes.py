def bfs(g, start):
    queue = [start]
    visited = []
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            queue.extend(g[node])

g = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print(g)
bfs(g, 'A')