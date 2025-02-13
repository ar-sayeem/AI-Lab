def bfs(g, start):
    stack = [start]
    visited = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            stack.extend(reversed(g[node]))  # Fixed missing parenthesis

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
