import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush

# Graph definition
graph = {
    'A': {'Z': 75, 'T': 118, 'S': 140}, 'Z': {'O': 71, 'A': 75}, 'O': {'S': 151, 'Z': 71},
    'T': {'L': 111, 'A': 118}, 'L': {'T': 111, 'M': 70}, 'M': {'L': 70, 'D': 75},
    'D': {'M': 75, 'C': 120}, 'C': {'D': 120, 'P': 138, 'R': 146},
    'S': {'O': 151, 'A': 140, 'F': 99, 'R': 80}, 'R': {'S': 80, 'C': 146, 'P': 97},
    'F': {'S': 99, 'B': 211}, 'P': {'R': 97, 'C': 138, 'B': 101},
    'B': {'F': 211, 'P': 101, 'G': 90, 'U': 85}, 'G': {'B': 90},
    'U': {'B': 85, 'H': 98, 'V': 142}, 'H': {'U': 98, 'E': 86}, 'E': {'H': 86},
    'V': {'U': 142, 'I': 92}, 'I': {'V': 92, 'N': 87}, 'N': {'I': 87}
}

# Heuristic values (Example: Straight-line distance to goal 'B')
heuristic = {
    'A': 366, 'Z': 374, 'O': 380, 'T': 329, 'L': 244, 'M': 241, 'D': 242, 'C': 160, 'S': 253, 'R': 193,
    'F': 178, 'P': 100, 'B': 0, 'G': 77, 'U': 80, 'H': 151, 'E': 161, 'V': 199, 'I': 226, 'N': 234
}

# Best First Search implementation
def best_first_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], start, [start])]
    visited = set()
    #print(priority_queue)

    while priority_queue:
        _, node, path = heappop(priority_queue)
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, {}):
                heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))
                #print(priority_queue)
    return None

# Perform Best First Search
start_node = 'A'
goal_node = 'B'
path_gbfs = best_first_search(graph, start_node, goal_node, heuristic)
print(f"Best First Search Path: {path_gbfs}")

# Visualization for Best First Search
def draw_graph_gbfs(graph, path, rotate_angle=0):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(12, 8))
    
    ax = plt.gca()
    if rotate_angle:
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        for key in pos:
            x, y = pos[key]
            pos[key] = (x * (abs(rotate_angle) / 90), y * (abs(rotate_angle) / 90))
    
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5)  # Highlight path
    
    plt.title("Best First Search Path Visualization", fontsize=12, fontweight='bold', color='darkblue')
    
    # Display path under the graph
    if path:
        plt.figtext(0.5, 0.01, f"GBFS Path: {path}", wrap=True, horizontalalignment='center', fontsize=12, color='darkblue')
    
    plt.show()

# Draw the graph with GBFS path
draw_graph_gbfs(graph, path_gbfs, rotate_angle=90)
