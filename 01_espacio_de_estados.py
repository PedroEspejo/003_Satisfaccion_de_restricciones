from collections import deque

def constraint_satisfaction_bfs(graph, colors):
    queue = deque()
    queue.append(list(graph.keys())[0])
    
    while queue:
        node = queue.popleft()
        if node not in colors:
            used_colors = set(colors[neighbor] for neighbor in graph[node] if neighbor in colors)
            for color in range(1, len(graph) + 1):
                if color not in used_colors:
                    colors[node] = color
                    break
            for neighbor in graph[node]:
                if neighbor not in colors:
                    queue.append(neighbor)

    return colors

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': []
}
colors = constraint_satisfaction_bfs(graph, {})
print("Asignación de colores:", colors)
