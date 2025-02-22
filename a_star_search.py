import heapq

def a_star(graph, start, goal, heuristic):
    pq = [(0, start, [start])]      # pq = priority queue
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

print(a_star(graph, 'A', 'B', heuristic))


# Actual Code
"""
import heapq

def a_star(graph, start, goal, heuristic):
    priority_queue = [(0, start, [start])]
    g_cost = {start: 0}

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        
        if node == goal:
            return path

        for neighbor, weight in graph.get(node, {}).items():
            new_cost = g_cost[node] + weight
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(priority_queue, (f_cost, neighbor, path + [neighbor]))
    
    return None

# Graph representation of the Romania map
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Timisoara': {'Lugoj': 111, 'Arad': 118},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Heuristic: Straight-line distance to Bucharest
heuristic = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176,
    'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329,
    'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

# Running A* Search
print(a_star(graph, 'Arad', 'Bucharest', heuristic))
"""
