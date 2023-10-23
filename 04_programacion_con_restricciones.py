from ortools.sat.python import cp_model

def graph_coloring_cp(graph, num_colors):
    model = cp_model.CpModel()
    colors = {}
    
    # Definición del grafo (mismo grafo que los ejemplos anteriores)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B'],
        'D': []
    }
    
    for node in graph:
        colors[node] = model.NewIntVar(1, num_colors, f'color_{node}')
    
    for node in graph:
        for neighbor in graph[node]:
            model.Add(colors[node] != colors[neighbor])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        return {node: solver.Value(colors[node]) for node in graph}
    return None

# Ejemplo de uso
num_colors = 3
colors = graph_coloring_cp(graph, num_colors)
if colors is not None:
    print("Asignación de colores:", colors)
else:
    print("No se encontró solución.")
