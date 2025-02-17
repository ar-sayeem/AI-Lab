import heapq

def best_first_search(graph, heuristic, start, goal):
    visited = set()
    priorityQ = []

    heapq.heappush(priorityQ, (heuristic[start], start))

    while priorityQ:
        _, current = heapq.heappop(priorityQ)

        if current == goal:
            print(f"{goal}")
            return
        
        if current not in visited:
            print(f"{current} -> ", end='')
            
            visited.add(current)

            for neighbor, _ in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(priorityQ, (heuristic[neighbor], neighbor))

    print("Goal not reachable.")


graph = {
    'Arad': [('Timisoara', 118), ('Zerind', 75), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu_Vilcea', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu_Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 138)],
    'Pitesti': [('Rimnicu_Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
    'Craiova': [('Dobreta', 120), ('Rimnicu_Vilcea', 146), ('Pitesti', 138)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86), ('Vaslui', 142)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}


heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu_Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

best_first_search(graph, heuristic, 'Arad', 'Bucharest')