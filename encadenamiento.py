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
