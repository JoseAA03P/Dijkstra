import tkinter as tk
from tkinter import Canvas, Frame

# Función para dibujar el grafo y el camino más corto.
def dibujar_grafo_y_camino(grafo, camino):
    root = tk.Tk()
    root.title("Grafo y Camino más Corto")

    canvas = Canvas(root, width=400, height=400)
    canvas.pack()

    # Dibuja los nodos del grafo.
    for i in range(len(grafo)):
        x = 50 + 100 * (i % 3)
        y = 50 + 100 * (i // 3)
        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue")
        canvas.create_text(x, y, text=str(i))

    # Dibuja las aristas del grafo.
    for i in range(len(grafo)):
        for j in range(i, len(grafo)):
            if grafo[i][j] > 0:
                x1 = 50 + 100 * (i % 3)
                y1 = 50 + 100 * (i // 3)
                x2 = 50 + 100 * (j % 3)
                y2 = 50 + 100 * (j // 3)
                canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)

    # Dibuja el camino más corto en rojo.
    for i in range(len(camino) - 1):
        nodo1 = camino[i]
        nodo2 = camino[i + 1]
        x1 = 50 + 100 * (nodo1 % 3)
        y1 = 50 + 100 * (nodo1 // 3)
        x2 = 50 + 100 * (nodo2 % 3)
        y2 = 50 + 100 * (nodo2 // 3)
        canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

    root.mainloop()

# Definición de la función Dijkstra que encuentra las distancias más cortas en un grafo desde un nodo inicial.
def dijkstra(grafo, nodo_inicial):
    # Obtenemos el número de nodos en el grafo.
    num_nodos = len(grafo)
    
    # Inicializamos tres listas: distancia, visitado y nodo_previo.
    distancia = [float('inf')] * num_nodos  # Inicializamos todas las distancias como infinito.
    visitado = [False] * num_nodos  # Inicializamos todos los nodos como no visitados.
    nodo_previo = [None] * num_nodos  # Inicializamos los nodos previos como indefinidos.

    # La distancia desde el nodo inicial a sí mismo es 0.
    distancia[nodo_inicial] = 0

    # Mientras haya nodos no visitados en el grafo.
    while any(not visitado[nodo] for nodo in range(num_nodos)):
        # Elegimos el nodo no visitado con la distancia más corta como nodo actual.
        nodo_actual = min((nodo for nodo in range(num_nodos) if not visitado[nodo]), key=lambda nodo: distancia[nodo])
        visitado[nodo_actual] = True  # Marcamos el nodo actual como visitado.

        # Iteramos sobre los vecinos del nodo actual.
        for vecino in range(num_nodos):
            if grafo[nodo_actual][vecino] > 0:
                # Calculamos la distancia temporal desde el nodo inicial al vecino a través del nodo actual.
                distancia_temporal = distancia[nodo_actual] + grafo[nodo_actual][vecino]
                
                # Si la distancia temporal es menor que la distancia actual almacenada en distancia[vecino], actualizamos la distancia.
                if distancia_temporal < distancia[vecino]:
                    distancia[vecino] = distancia_temporal
                    nodo_previo[vecino] = nodo_actual  # Actualizamos el nodo previo.

    # Al final, retornamos las listas de distancias y nodos previos.
    return distancia, nodo_previo

# Definimos el grafo de entrada como una lista de listas (matriz de adyacencia).
grafo = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]


nodo_inicial = 0
distancias, nodos_previos = dijkstra(grafo, nodo_inicial)
nodo_destino = 4  # Cambia esto al nodo de destino que desees

# Imprimimos las distancias más cortas desde el nodo inicial a todos los demás nodos.
print("Distancias más cortas desde el nodo inicial:")
for nodo, distancia in enumerate(distancias):
    print(f"Nodo {nodo}: Distancia = {distancia}")

    
# Recupera el camino más corto desde el nodo inicial al nodo de destino.
camino_mas_corto = []
while nodo_destino is not None:
    camino_mas_corto.insert(0, nodo_destino)
    nodo_destino = nodos_previos[nodo_destino]

# Llama a la función para dibujar el grafo y el camino más corto.
dibujar_grafo_y_camino(grafo, camino_mas_corto)
