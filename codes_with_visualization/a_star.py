import heapq            # priority queue
import networkx as nx
import matplotlib.pyplot as plt

def a_star(graph, start, goal, heuristic):
    pq = [(0, start, [start])]
    g_cost = {start: 0}
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        
        for neighbor, weight in graph.get(node, {}).items():
            new_cost = g_cost[node] + weight
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                heapq.heappush(pq, (new_cost + heuristic[neighbor], neighbor, path + [neighbor]))
    
    return None

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

heuristic = {'A': 366, 'B': 0, 'C': 160, 'D': 242, 'E': 161, 'F': 176,
    'G': 77, 'H': 151, 'I': 226, 'L': 244, 'M': 241, 'N': 234,
    'O': 380, 'P': 100, 'R': 193, 'S': 253, 'T': 329,
    'U': 80, 'V': 199, 'Z': 374}

# Perform A* Search
start_node = 'A'
goal_node = 'B'
path = a_star(graph, start_node, goal_node, heuristic)
print(f"A* Path: {path}")

# Visualization
def draw_graph_a_star(graph, path, rotate_angle=0):
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
    
    plt.title("A* Search Path Visualization", fontsize=12, fontweight='bold', color='darkblue')
    
    # Display path under the graph
    if path:
        plt.figtext(0.5, 0.01, f"A* Path: {path}", wrap=True, horizontalalignment='center', fontsize=12, color='darkblue')
    
    plt.show()

# Draw the graph with A* path
draw_graph_a_star(graph, path, rotate_angle=90)
