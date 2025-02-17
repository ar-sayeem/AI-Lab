import networkx as nx
import matplotlib.pyplot as plt

# Given graph representation
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

# DFS function to find the shortest path to any leaf
def dfs_shortest_leaf(graph, start):
    stack = [(start, 0, [start])]  # (current node, cost, path)
    shortest_path = None
    min_cost = float('inf')
    
    while stack:
        node, cost, path = stack.pop()
        
        if not graph[node]:  # If leaf node
            if cost < min_cost:
                min_cost = cost
                shortest_path = path
        else:
            for neighbor, weight in graph[node].items():
                stack.append((neighbor, cost + weight, path + [neighbor]))
    
    return shortest_path

# Get the shortest path from root to any leaf
shortest_leaf_path = dfs_shortest_leaf(Graph, 'A')
shortest_edges = [(shortest_leaf_path[i], shortest_leaf_path[i+1]) for i in range(len(shortest_leaf_path)-1)]

# Create a new directed graph for visualization
G_tree = nx.DiGraph()

# Adding edges
for node, neighbors in Graph.items():
    for neighbor, weight in neighbors.items():
        G_tree.add_edge(node, neighbor, weight=weight)

# Corrected tree layout for visualization
pos_tree = {
    'A': (4, 5), 'B': (2, 4), 'C': (6, 4), 'D': (1, 3), 'E': (3, 3), 'F': (5, 3), 'G': (7, 3),
    'H': (0, 2), 'I': (2, 2), 'J': (3, 2), 'K': (4, 2), 'L': (5, 2), 'M': (6, 2), 'N': (7, 2), 'O': (8, 2)
}

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G_tree, pos_tree, with_labels=True, node_color='lightblue', edge_color='black', node_size=2000, font_size=10)

# Highlight the shortest path from root to a leaf in red
nx.draw_networkx_edges(G_tree, pos_tree, edgelist=shortest_edges, edge_color='red', width=2)

# Add edge labels
edge_labels_tree = {(u, v): d['weight'] for u, v, d in G_tree.edges(data=True)}
nx.draw_networkx_edge_labels(G_tree, pos_tree, edge_labels=edge_labels_tree, font_size=10, font_color='black')

# Display the graph
plt.title("Tree Structure with Shortest Root-to-Leaf Path Highlighted in Red")
plt.show()
