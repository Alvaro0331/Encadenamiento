import matplotlib.pyplot as plt
import networkx as nx

#Definir valores de los nodos
nodo={
    "A": None,"B":None,"C":None,"D":True,"E":True,"F":True,
    "G":None,"H":None,"I":None,"J":None,"K":None,"L":True,"M":None
}

#Reglas de inferencia
reglas={
    "C":["A","B"],
    "G":["D","E","F"],
    "J":["H","I"],
    "K":["C","G"],
    "L":["G","J"],
    "M":["K","L"],   
}

#Funcion de encadenamiento
def encadenamiento(objetivo):
    #Identificar si ya conocemos el valor del objetivo
    if nodo[objetivo] is not None:
        return nodo[objetivo]
    
    #Identificar si se puede inferir su valor a partir de las reglas
    if objetivo in reglas:
        dependencias=reglas[objetivo]
        #print(f"Evaluando {objetivo} con {dependencias}")
        valor_premisas=[]
        for premisa in dependencias:
            #Recursion
            valor_premisa=encadenamiento(premisa)
            valor_premisas.append(valor_premisa)
        
        #Identificar si todas las premisas son verdaderas
        if all(valor_premisas):
            nodo[objetivo]=True
            return True
        #Si alguna premisa es falsa, el objetivo actual tambien es falso
        else:
            nodo[objetivo]=False
            return False
    
    #Preguntar al usuario por el valor de un dodo
    respuesta=input(f"{objetivo} es Verdadero o Falso? (V/F): ").strip().lower()
    #Asignar el valor proporcionado al nodo
    nodo[objetivo]= True if respuesta =="v" else False
    return nodo[objetivo]


#Test
objetivo="M"
valor=encadenamiento(objetivo)
print(f"El {objetivo} es {valor}")

#Creamos el grafo a mostrar
G=nx.DiGraph()

for nodo_destino,(dependencias) in reglas.items():
    for dependencia in dependencias:
        G.add_edge(dependencia,nodo_destino)

#Dar colores a los nodos
colores={True:"lightgreen", False:"lightcoral",None:"lightgray"}
node_colors=[colores[nodo[n]] for n in G.nodes]

# Dibujar el árbol
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color=node_colors, edge_color="gray", font_size=10, font_weight="bold")
#Etiquetas de los nodos y sus valores
node_labels = {n: f"\n({str(nodo[n])})" for n in G.nodes}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_weight="bold")
plt.title("Encadenamiento")
plt.show()