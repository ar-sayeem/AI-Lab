import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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

# BFS Search
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    print(queue)

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, {}):
                queue.append((neighbor, path + [neighbor]))
                print(queue)

    return None

# Perform BFS Search
start_node = 'A'
goal_node = 'B'
path_bfs = bfs(graph, start_node, goal_node)
print(f"BFS Path: {path_bfs}")

# Visualization for BFS Search
def draw_graph_bfs(graph, path, rotate_angle=0):
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
    
    plt.title("BFS Search Path Visualization", fontsize=12, fontweight='bold', color='darkblue')
    
    # Display path under the graph
    if path:
        plt.figtext(0.5, 0.01, f"BFS Path: {path}", wrap=True, horizontalalignment='center', fontsize=12, color='darkblue')
    
    plt.show()

# Draw the graph with BFS path
draw_graph_bfs(graph, path_bfs, rotate_angle=90)
