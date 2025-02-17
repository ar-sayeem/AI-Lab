def dfs(g, start):
    stack = [start]
    visited = []
    
    while stack:
        node = stack.pop()  # LIFO behavior
        if node not in visited:
            print(node, end=' ')
            visited.append(node)
            stack.extend(reversed(g[node]))  # Reverse to maintain order

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
dfs(g, 'A')  # Expected output: A B D E C F G
