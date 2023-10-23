def constraint_satisfaction_backtracking(graph, colors, node):
    if node not in colors:
        used_colors = set(colors[neighbor] for neighbor in graph[node] if neighbor in colors)
        for color in range(1, len(graph) + 1):
            if color not in used_colors:
                colors[node] = color
                break
        for neighbor in graph[node]:
            if neighbor not in colors:
                if not constraint_satisfaction_backtracking(graph, colors, neighbor):
                    return False
    return True

# Definición del grafo (mismo grafo que los ejemplos anteriores)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': []
}

# Ejemplo de uso
colors = {}
if not constraint_satisfaction_backtracking(graph, colors, list(graph.keys())[0]):
    print("No se encontró solución.")
else:
    print("Asignación de colores:", colors)
