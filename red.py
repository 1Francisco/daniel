import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt # Importamos matplotlib para dibujar el grafo

# --- Parte Existente del Código ---

data = pd.read_excel("red dirigida.xlsx")
# hacer arrays
#for i in data:
 #   print(i)
df = np.array(data)
# print(df)
# print(df.shape)



a = np.triu(df,1)

a = a + np.transpose(a)
# print(a) # Imprimimos 'a' (matriz de adyacencia) al final de esta sección.

particion = 10
I = np.zeros((20,1))
E = np.zeros((20,1))
# print(I.shape)
# print(E.shape)
# print(I)
for i in range(len(a)):
    for j in range(len(a)):
        if i < particion and j < particion:
            I[i] += a[i][j]
            
        elif i >= particion and j >= particion:
            I[i] += a[i][j]
        elif i < particion and j >= particion:
            E[i] += a[i][j]
            
        else:
            E[i] += a[i][j]
# print(I)
# print(E)
D = E - I

# --- Nuevo Código para Graficar ---

## 📊 Creación y Visualización del Grafo

# 1. Crear el objeto grafo (no dirigido, ya que 'a' es simétrica)
# 'a' debe ser la matriz de adyacencia del grafo.
# Usaremos nx.from_numpy_array para crear el grafo a partir de la matriz.
G = nx.from_numpy_array(a)

# 2. Definir las particiones de los nodos (índices de 0 a 19)
# Los nodos con índice < 10 pertenecen al Grupo 1.
# Los nodos con índice >= 10 pertenecen al Grupo 2.
nodes_group1 = list(range(particion)) # Nodos 0 a 9
nodes_group2 = list(range(particion, len(a))) # Nodos 10 a 19

# 3. Asignar atributos y colores a los nodos
# Lista de colores: 'red' para el Grupo 1, 'blue' para el Grupo 2.
# Asignamos un color a cada nodo según su índice.
node_colors = []
for node in G.nodes():
    if node < particion:
        G.nodes[node]['group'] = 1
        node_colors.append('red') # Color para el Grupo 1
    else:
        G.nodes[node]['group'] = 2
        node_colors.append('blue') # Color para el Grupo 2

# 4. Definir la disposición (layout) de los nodos para la visualización
# Esto ayuda a que el grafo se vea bien organizado. El 'spring_layout' es común.
pos = nx.spring_layout(G, seed=42) # Usar una semilla (seed) para resultados reproducibles

# 5. Dibujar el grafo
plt.figure(figsize=(12, 12))
plt.title("Grafo con Nodos Particionados (Grupos 1 y 2)")

# Dibujar los nodos con sus colores respectivos
nx.draw_networkx_nodes(G, pos, 
                       node_color=node_colors, 
                       node_size=500, # Tamaño de los nodos
                       alpha=0.8)

# Dibujar las aristas (conexiones)
nx.draw_networkx_edges(G, pos, 
                       width=1.0, 
                       alpha=0.5)

# Dibujar las etiquetas de los nodos (los números de nodo)
nx.draw_networkx_labels(G, pos, 
                        font_size=10, 
                        font_color="black")

# Crear una leyenda manual para los grupos
legend_handles = [
    plt.Line2D([0], [0], marker='o', color='w', label='Grupo 1 (Nodos 0-9)', 
               markerfacecolor='red', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Grupo 2 (Nodos 10-19)', 
               markerfacecolor='blue', markersize=10)
]

plt.legend(handles=legend_handles, loc='upper left')

plt.axis('off') # Ocultar los ejes de matplotlib
plt.show() # Mostrar el grafo
