def ac3(graph, colors):
    queue = [(node, neighbor) for node in graph for neighbor in graph[node]]
    while queue:
        node, neighbor = queue.pop(0)
        if revise(graph, colors, node, neighbor):
            if not colors[node]:
                continue
            if not graph[node]:
                return False
            for n in graph[node]:
                if n != neighbor:
                    queue.append((n, node))
    return True

def revise(graph, colors, node, neighbor):
    revised = False
    for color in colors[node]:
        if not any(color != colors[neighbor][n] for n in graph[neighbor]):
            colors[node].remove(color)
            revised = True
    return revised

# Definición del grafo (mismo grafo que los ejemplos anteriores)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': []
}

# Ejemplo de uso
num_colors = 3
colors = {node: list(range(1, num_colors + 1)) for node in graph}
if ac3(graph, colors):
    print("Asignación de colores:", colors)
else:
    print("No se encontró solución.")
