# def dfs_total_cost(graph):
#     total_cost = 0
#     for node in graph:
#         total_cost += sum(graph[node].values())
#     return total_cost


# def dfs_min_cost_path(graph, start):
#     stack = [(start, [start], 0)]  # (current_node, path, cost)
#     min_cost = float('inf')
#     min_path = []
    
#     while stack:
#         node, path, cost = stack.pop()
        
#         if not graph[node]:  # If leaf node
#             if cost < min_cost:
#                 min_cost = cost
#                 min_path = path
        
#         for neighbor, edge_cost in graph[node].items():
#             stack.append((neighbor, path + [neighbor], cost + edge_cost))
    
#     return min_cost, min_path


# # Given tree graph
# graph = {
#     'A': {'B': 1, 'C': 2},
#     'B': {'D': 1, 'E': 2},
#     'C': {'F': 3, 'G': 4},
#     'D': {'H': 2, 'I': 1},
#     'E': {'J': 4, 'K': 3},
#     'F': {'L': 2, 'M': 3},
#     'G': {'N': 1, 'O': 1},
#     'H': {},
#     'I': {},
#     'J': {},    
#     'K': {},
#     'L': {},
#     'M': {},
#     'N': {},
#     'O': {}
# }

# total_cost = dfs_total_cost(graph)
# min_cost, min_path = dfs_min_cost_path(graph, 'A')

# print("Total cost of the tree:", total_cost)
# print("Minimum cost path:", min_path, "with cost:", min_cost)

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
    
    pos = {
        'A': (4, 8), 'B': (2, 6), 'C': (6, 6), 'D': (1, 4), 'E': (3, 4), 'F': (5, 4), 'G': (7, 4),
        'H': (0, 2), 'I': (2, 2), 'J': (2, 2), 'K': (4, 2), 'L': (4, 2), 'M': (6, 2), 'N': (6, 2), 'O': (8, 2)
    }
    
    # labels = nx.get_edge_attributes(G, 'weight')
    # plt.figure(figsize=(8, 6))
    # nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # plt.title("Tree Graph Visualization", fontsize=12, fontweight='bold', color='darkblue')
    # plt.show()

    # labels = nx.get_edge_attributes(G, 'weight')
    # plt.figure(figsize=(8, 6))
    # edges = G.edges()
    # edge_colors = ['red' if (u in min_path and v in min_path and min_path.index(u) + 1 == min_path.index(v)) else 'gray' for u, v in edges]
    
    # nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold', edge_color=edge_colors, width=2)
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # plt.title("Tree Graph Visualization", fontsize=12, fontweight='bold', color='darkblue')
    # plt.show()

    plt.figure(figsize=(8, 6))
    
    # Highlight shortest path in red, others in gray
    edge_colors = ['red' if (u, v) in zip(min_path, min_path[1:]) or (v, u) in zip(min_path, min_path[1:]) else 'gray' for u, v in G.edges()]
    
    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold', edge_color=edge_colors, width=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    
    plt.title("Tree Graph Visualization", fontsize=12, fontweight='bold', color='darkblue')
    plt.show()


draw_graph(graph)
