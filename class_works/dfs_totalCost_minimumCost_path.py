# Without Visualization
"""
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
"""


# With Visualization

#from matplotlib.offsetbox import OffsetImage, AnnotationBbox

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

# Visualization Code
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    
    # Updated positions with properly separated leaf nodes
    pos = {
        'A': (4, 8), 
        'B': (2, 6), 
        'C': (6, 6), 
        'D': (1, 4), 
        'E': (3, 4), 
        'F': (5, 4), 
        'G': (7, 4),
        'H': (0.25, 2), # H-I distance = 1.25
        'I': (1.5, 2),  # I-J = .75
        'J': (2.25, 2), # J-K distance = 1.25
        'K': (3.75, 2), # K-l = .75
        'L': (4.5, 2),  # L-M distance = 1.25
        'M': (5.75, 2), # M-N = .75
        'N': (6.5, 2),  # N-O distance = 1.25
        'O': (7.75, 2)
    }
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Highlight shortest path in red, others in gray
    edge_colors = ['red' if (u, v) in zip(min_path, min_path[1:]) or (v, u) in zip(min_path, min_path[1:]) else 'gray' for u, v in G.edges()]
    
    # Draw the graph
    nx.draw(G, pos, ax=ax, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold', edge_color=edge_colors, width=2)
    nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=nx.get_edge_attributes(G, 'weight'))

    plt.title("DFS Minimum Cost Path Visualization", fontsize=16, fontweight='bold', color='darkblue')
    
    # Display path and total cost under the graph
    path_text = f"Minimum Cost Path: {' → '.join(min_path)} (Cost: {min_cost})"
    total_cost_text = f"Total Cost of The Tree: {total_cost}"
    
    plt.figtext(0.5, 0.07, path_text, wrap=True, horizontalalignment='center', fontsize=14, color='darkblue')
    plt.figtext(0.5, 0.10, total_cost_text, wrap=True, horizontalalignment='center', fontsize=14, color='darkblue')
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)  # Increased bottom margin to make room for both text lines
    plt.show()

draw_graph(graph)