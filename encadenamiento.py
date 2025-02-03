



#Definir valores de los nodos
nodo={
    "A": None,
    "B":None,
    "C":None,
    "D":True,
    "E":True,
    "F":True,
    "G":None,
    "H":None,
    "I":None,
    "J":None,
    "K":None,
    "L":True,
    "M":None
}

#Regla 1
if nodo["A"] is True and nodo["B"] is True:
    nodo["C"] is True
    
#Regla 2
if nodo["D"] is True and nodo["E"] is True and nodo["F"] is True:
    nodo["G"] is True
    
#Regla 3
if nodo["H"] is True and nodo["I"] is True:
    nodo["J"] is True
    
#Relga 4
if nodo["C"] is True and nodo["G"] is True:
    nodo["K"] is True
    
#Regla 5
if nodo["G"] is True and nodo["J"] is True:
    nodo["L"] is True
    
#Regla 6
if nodo["K"] is True and nodo["L"] is True:
    nodo["M"] is True